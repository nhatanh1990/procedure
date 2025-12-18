#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script để generate index.html từ tất cả file markdown
"""

import os
import json

def get_file_content(filepath):
    """Đọc nội dung file với encoding UTF-8"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Remove BOM if present
            if content.startswith('\ufeff'):
                content = content[1:]
            return content
    except Exception as e:
        return f'Error reading file: {str(e)}'

def get_all_markdown_files(root_dir):
    """Lấy tất cả file .md trong thư mục"""
    files = []
    for root, dirs, filenames in os.walk(root_dir):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for filename in filenames:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)
                rel_path = os.path.relpath(filepath, root_dir)
                files.append((rel_path, filepath))
    return sorted(files)

def get_file_priority(rel_path):
    """Xác định priority để sắp xếp"""
    filename = os.path.basename(rel_path)
    folder = os.path.dirname(rel_path)
    
    if folder == '':
        priority_map = {
            'README.md': 1,
            'HUONG_DAN_SU_DUNG_NHANH.md': 2,
            'BEST_PRACTICES.md': 3,
            'QUICK_REFERENCE_THAY_DOI.md': 4,
            'QUICK_REFERENCE_QUYEN_TRUY_CAP.md': 5,
            'CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md': 6,
        }
        return priority_map.get(filename, 50)
    
    priority_map = {
        'QT-002-QUAN_TRI_VAN_HANH.md': 100, 'QT-003-UPCODE.md': 101, 'QT-004-HOTFIX.md': 102,
        'QT-005-PROVISIONING.md': 103, 'QT-006-VERSIONING.md': 104, 'QT-007-RELEASE_SAN_PHAM.md': 105,
        'QT-008-DANH_SACH_THAY_DOI_CHUAN.md': 106, 'QT-009-QUY_TRINH_BO_SUNG_THAY_DOI.md': 107,
        'QT-010-RA_SOAT_HE_THONG_AUDIT.md': 108,
        'CL-001-CHECKLIST_VAN_HANH.md': 200, 'CL-002-CHECKLIST_UPCODE.md': 201, 'CL-003-CHECKLIST_HOTFIX.md': 202,
        'CL-004-CHECKLIST_PROVISIONING.md': 203, 'CL-005-CHECKLIST_RELEASE.md': 204, 'CL-006-TRA_CUU_THAY_DOI.md': 205,
        'CL-007-CHECKLIST_NHOM_A_HATANG.md': 206, 'CL-008-CHECKLIST_NHOM_B_UNG_DUNG.md': 207,
        'CL-009-CHECKLIST_NHOM_C_DULIEU.md': 208, 'CL-010-CHECKLIST_NHOM_D_SUCO.md': 209, 'CL-011-CHECKLIST_QUYEN_TRUY_CAP.md': 210,
        'CL-012-CHECKLIST_RA_SOAT_HE_THONG.md': 211,
        'TP-001-TEMPLATE_RFC.md': 300, 'TP-001-EXAMPLE_RFC.md': 301, 'TP-002-TEMPLATE_HOTFIX.md': 302,
        'TP-002-EXAMPLE_HOTFIX.md': 303, 'TP-003-TEMPLATE_RELEASE_NOTE.md': 304, 'TP-003-EXAMPLE_RELEASE_NOTE.md': 305,
        'TP-004-TEMPLATE_PROVISIONING.md': 306, 'TP-004-EXAMPLE_PROVISIONING.md': 307, 'TP-005-TEMPLATE_TRA_CUU_THAY_DOI.md': 308,
        'TP-005-EXAMPLE_TRA_CUU_THAY_DOI.md': 309, 'TP-006-TEMPLATE_YEU_CAU_CAP_QUYEN.md': 310, 'TP-006-EXAMPLE_YEU_CAU_CAP_QUYEN.md': 311,
        'TP-007-TEMPLATE_BAO_CAO_RA_SOAT.md': 312, 'TP-007-EXAMPLE_BAO_CAO_RA_SOAT.md': 313,
        'TP-008-TEMPLATE_KE_HOACH_HANH_DONG.md': 314, 'TP-008-EXAMPLE_KE_HOACH_HANH_DONG.md': 315,
        'QUICK_START.md': 400, 'HUONG_DAN_SU_DUNG_QUYEN_TRUY_CAP.md': 401, 'TROUBLESHOOTING.md': 402,
        'CHANGELOG.md': 403, 'HUONG_DAN_CHANGELOG.md': 404, 'HUONG_DAN_TRAINING.md': 405, 'METADATA_CONFIG.md': 406,
    }
    if filename in priority_map:
        return priority_map[filename]
    
    if 'Quy trình' in folder:
        return 150
    elif 'Checklist' in folder:
        return 250
    elif 'Template' in folder:
        return 350
    elif 'Hỗ trợ' in folder or 'Support' in folder:
        return 450
    else:
        return 500

def get_category_info(rel_path):
    """Xác định category cho navigation"""
    filename = os.path.basename(rel_path)
    folder = os.path.dirname(rel_path)
    
    if folder == '':
        return {'category': 'Root', 'order': 1, 'display_name': filename}
    elif 'Quy trình' in folder:
        return {'category': 'Quy trình (QT-XXX)', 'order': 2, 'display_name': filename}
    elif 'Checklist' in folder:
        return {'category': 'Checklist (CL-XXX)', 'order': 3, 'display_name': filename}
    elif 'Template' in folder:
        return {'category': 'Template (TP-XXX)', 'order': 4, 'display_name': filename}
    elif 'Hỗ trợ' in folder or 'Support' in folder:
        return {'category': 'Hỗ trợ (Support)', 'order': 5, 'display_name': filename}
    else:
        return {'category': 'Khác', 'order': 6, 'display_name': filename}

def main():
    root_dir = '.'
    md_files = get_all_markdown_files(root_dir)
    file_structure = {}
    navigation = []
    
    print(f"Đang xử lý {len(md_files)} file markdown...")
    
    for rel_path, full_path in md_files:
        content = get_file_content(full_path)
        file_structure[rel_path] = content
        priority = get_file_priority(rel_path)
        category_info = get_category_info(rel_path)
        navigation.append({
            'path': rel_path,
            'category': category_info['category'],
            'category_order': category_info['order'],
            'name': category_info['display_name'],
            'display': rel_path.replace(os.sep, ' / '),
            'priority': priority
        })
    
    navigation.sort(key=lambda x: (x['category_order'], x['priority']))
    
    # Serialize JSON
    files_json = json.dumps(file_structure, ensure_ascii=False)
    nav_json = json.dumps(navigation, ensure_ascii=False)
    
    # Read HTML template
    html_template = '''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hệ Thống Quy Trình và Quy Định - Tài Liệu</title>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
            display: flex;
            height: 100vh;
            overflow: hidden;
        }
        
        .sidebar {
            width: 320px;
            background: #2c3e50;
            color: white;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            box-shadow: 2px 0 5px rgba(0,0,0,0.1);
        }
        
        .sidebar-header {
            padding: 20px;
            background: #1a252f;
            border-bottom: 1px solid #34495e;
            position: sticky;
            top: 0;
            z-index: 10;
        }
        
        .sidebar-header h1 {
            font-size: 18px;
            margin-bottom: 10px;
        }
        
        .search-box {
            width: 100%;
            padding: 10px;
            border: 1px solid #34495e;
            border-radius: 4px;
            background: #34495e;
            color: white;
            font-size: 14px;
        }
        
        .search-box::placeholder {
            color: #95a5a6;
        }
        
        .nav-section {
            flex: 1;
            overflow-y: auto;
            padding: 10px 0;
        }
        
        .nav-category {
            margin-bottom: 15px;
        }
        
        .nav-category-title {
            padding: 10px 20px;
            font-weight: bold;
            font-size: 12px;
            text-transform: uppercase;
            color: #95a5a6;
            background: #1a252f;
            position: sticky;
            top: 0;
            z-index: 5;
        }
        
        .nav-item {
            padding: 8px 20px 8px 30px;
            cursor: pointer;
            transition: background 0.2s;
            font-size: 13px;
            border-left: 3px solid transparent;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .nav-item:hover {
            background: #34495e;
        }
        
        .nav-item.active {
            background: #3498db;
            border-left-color: #2980b9;
        }
        
        .nav-item-number {
            color: #95a5a6;
            font-weight: bold;
            min-width: 25px;
        }
        
        .nav-item.active .nav-item-number {
            color: white;
        }
        
        .nav-item-name {
            flex: 1;
            word-break: break-word;
        }
        
        .main-content {
            flex: 1;
            overflow-y: auto;
            background: white;
            padding: 40px;
        }
        
        .content-header {
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 2px solid #ecf0f1;
        }
        
        .content-header h1 {
            font-size: 32px;
            color: #2c3e50;
            margin-bottom: 10px;
        }
        
        .file-path {
            color: #7f8c8d;
            font-size: 14px;
            font-family: monospace;
        }
        
        .markdown-content {
            max-width: 900px;
        }
        
        .markdown-content h1 {
            font-size: 28px;
            margin: 30px 0 20px;
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        
        .markdown-content h2 {
            font-size: 24px;
            margin: 25px 0 15px;
            color: #34495e;
        }
        
        .markdown-content h3 {
            font-size: 20px;
            margin: 20px 0 12px;
            color: #34495e;
        }
        
        .markdown-content h4 {
            font-size: 18px;
            margin: 15px 0 10px;
            color: #34495e;
        }
        
        .markdown-content p {
            margin: 15px 0;
        }
        
        .markdown-content table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        .markdown-content table th {
            background: #34495e;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: bold;
        }
        
        .markdown-content table td {
            padding: 10px 12px;
            border-bottom: 1px solid #ecf0f1;
        }
        
        .markdown-content table tr:hover {
            background: #f8f9fa;
        }
        
        .markdown-content code {
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }
        
        .markdown-content pre {
            background: #2c3e50;
            color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            margin: 20px 0;
        }
        
        .markdown-content pre code {
            background: none;
            padding: 0;
            color: inherit;
        }
        
        .markdown-content blockquote {
            border-left: 4px solid #3498db;
            padding-left: 20px;
            margin: 20px 0;
            color: #7f8c8d;
            font-style: italic;
        }
        
        .markdown-content ul, .markdown-content ol {
            margin: 15px 0;
            padding-left: 30px;
        }
        
        .markdown-content li {
            margin: 8px 0;
        }
        
        .markdown-content hr {
            border: none;
            border-top: 2px solid #ecf0f1;
            margin: 30px 0;
        }
        
        .markdown-content a {
            color: #3498db;
            text-decoration: none;
        }
        
        .markdown-content a:hover {
            text-decoration: underline;
        }
        
        .markdown-content .mermaid {
            background: white;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
            border: 1px solid #ecf0f1;
            text-align: center;
            overflow-x: auto;
        }
        
        @media (max-width: 768px) {
            body {
                flex-direction: column;
            }
            
            .sidebar {
                width: 100%;
                height: 200px;
            }
            
            .main-content {
                padding: 20px;
            }
        }
        
        .loading {
            text-align: center;
            padding: 50px;
            color: #7f8c8d;
        }
        
        .empty-state {
            text-align: center;
            padding: 50px;
            color: #7f8c8d;
        }
    </style>
</head>
<body>
    <div class="sidebar">
        <div class="sidebar-header">
            <h1>Tài Liệu</h1>
            <input type="text" id="searchBox" class="search-box" placeholder="Tìm kiếm...">
        </div>
        <div class="nav-section" id="navSection">
            <div class="loading">Đang tải...</div>
        </div>
    </div>
    <div class="main-content">
        <div id="mainContent">
            <div class="loading">Đang tải nội dung...</div>
        </div>
    </div>
    <script id="files-data" type="application/json">'''
    
    # Complete HTML
    html_content = html_template + files_json + '''</script>
    <script id="navigation-data" type="application/json">''' + nav_json + '''</script>
    <script>
        // Initialize Mermaid
        if (typeof mermaid !== 'undefined') {
            mermaid.initialize({ startOnLoad: false, theme: 'default' });
        }
        
        // Load data from script tags
        let files = {};
        let navigation = [];
        
        try {
            const filesElement = document.getElementById('files-data');
            const navElement = document.getElementById('navigation-data');
            
            if (filesElement && navElement) {
                files = JSON.parse(filesElement.textContent);
                navigation = JSON.parse(navElement.textContent);
                console.log('Loaded', Object.keys(files).length, 'files and', navigation.length, 'navigation items');
            } else {
                console.error('Cannot find data script tags');
            }
        } catch (e) {
                console.error('Error loading data:', e);
        }
        
        // Current file
        let currentFile = 'README.md';
        
        // Initialize
        function init() {
            if (Object.keys(files).length === 0) {
                document.getElementById('mainContent').innerHTML = '<div class="empty-state"><h2>Lỗi tải dữ liệu</h2><p>Không thể tải dữ liệu từ file. Vui lòng kiểm tra console (F12).</p></div>';
                return;
            }
            renderNavigation();
            renderFile(currentFile);
            setupSearch();
        }
        
        // Render navigation
        function renderNavigation(filter) {
            if (!filter) filter = '';
            const navSection = document.getElementById('navSection');
            if (!navSection) return;
            
            const categories = {};
            let itemNumber = 1;
            
            navigation.forEach(function(item) {
                const name = item.name.toLowerCase();
                const display = item.display.toLowerCase();
                const filterLower = filter.toLowerCase();
                if (filter && !name.includes(filterLower) && !display.includes(filterLower)) {
                    return;
                }
                
                if (!categories[item.category]) {
                    categories[item.category] = [];
                }
                categories[item.category].push({
                    path: item.path,
                    name: item.name,
                    number: itemNumber++
                });
            });
            
            let html = '';
            const categoryOrder = ['Root', 'Quy trình (QT-XXX)', 'Checklist (CL-XXX)', 'Template (TP-XXX)', 'Hỗ trợ (Support)', 'Khác'];
            categoryOrder.forEach(function(category) {
                if (categories[category] && categories[category].length > 0) {
                    html += '<div class="nav-category">';
                    html += '<div class="nav-category-title">' + category + '</div>';
                    categories[category].forEach(function(item) {
                        const active = item.path === currentFile ? 'active' : '';
                        const escapedPath = item.path.replace(/'/g, "\\'").replace(/"/g, '&quot;').replace(/\\\\/g, '\\\\\\\\');
                        html += '<div class="nav-item ' + active + '" onclick="renderFile(\\'' + escapedPath + '\\')">';
                        html += '<span class="nav-item-number">' + item.number + '</span>';
                        html += '<span class="nav-item-name">' + item.name + '</span>';
                        html += '</div>';
                    });
                    html += '</div>';
                }
            });
            
            navSection.innerHTML = html;
        }
        
        // Render file content
        function renderFile(filePath) {
            const mainContent = document.getElementById('mainContent');
            if (!mainContent) return;
            
            if (!files || !files[filePath]) {
                mainContent.innerHTML = '<div class="empty-state"><h2>File không tìm thấy</h2><p>File: ' + filePath + '</p></div>';
                return;
            }
            
            currentFile = filePath;
            const content = files[filePath];
            
            // Configure marked
            if (typeof marked !== 'undefined') {
                marked.setOptions({
                    breaks: true,
                    gfm: true
                });
            }
            
            // Process mermaid code blocks BEFORE markdown parsing
            let processedContent = content;
            const mermaidRegex = /```mermaid\\s*\\n([\\s\\S]*?)```/g;
            const mermaidBlocks = [];
            let mermaidIndex = 0;
            
            processedContent = processedContent.replace(mermaidRegex, function(match, diagram) {
                const id = 'mermaid-' + mermaidIndex++;
                const cleanDiagram = diagram.trim();
                mermaidBlocks.push({ id: id, diagram: cleanDiagram });
                return '<div class="mermaid" id="' + id + '">' + cleanDiagram + '</div>';
            });
            
            // Parse markdown
            let html = '';
            if (typeof marked !== 'undefined') {
                html = marked.parse(processedContent);
            } else {
                html = '<pre>' + processedContent + '</pre>';
            }
            
            const fileName = getFileName(filePath);
            mainContent.innerHTML = '<div class="content-header"><h1>' + escapeHtml(fileName) + '</h1><div class="file-path">' + escapeHtml(filePath) + '</div></div><div class="markdown-content">' + html + '</div>';
            
            // Render mermaid diagrams AFTER content is in DOM
            setTimeout(function() {
                mermaidBlocks.forEach(function(block) {
                    const element = document.getElementById(block.id);
                    if (element && typeof mermaid !== 'undefined') {
                        try {
                            mermaid.render(block.id + '-svg', block.diagram).then(function(result) {
                                element.innerHTML = result.svg;
                            }).catch(function(err) {
                                console.error('Mermaid render error:', err);
                                element.innerHTML = '<pre style="color: red;">Mermaid Error: ' + escapeHtml(err.message) + '\\n\\n' + escapeHtml(block.diagram) + '</pre>';
                            });
                        } catch (err) {
                            console.error('Mermaid render error:', err);
                            element.innerHTML = '<pre style="color: red;">Mermaid Error: ' + escapeHtml(err.message) + '\\n\\n' + escapeHtml(block.diagram) + '</pre>';
                        }
                    }
                });
            }, 100);
            
            // Update active nav item
            const searchBox = document.getElementById('searchBox');
            renderNavigation(searchBox ? searchBox.value : '');
            
            // Scroll to top
            const mainContentEl = document.querySelector('.main-content');
            if (mainContentEl) {
                mainContentEl.scrollTop = 0;
            }
        }
        
        // Get file name from path
        function getFileName(path) {
            const parts = path.split('/');
            return parts[parts.length - 1].replace('.md', '');
        }
        
        // Escape HTML
        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }
        
        // Setup search
        function setupSearch() {
            const searchBox = document.getElementById('searchBox');
            if (!searchBox) return;
            
            let searchTimeout;
            searchBox.addEventListener('input', function(e) {
                clearTimeout(searchTimeout);
                searchTimeout = setTimeout(function() {
                    renderNavigation(e.target.value);
                }, 300);
            });
        }
        
        // Initialize on load
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', init);
        } else {
            init();
        }
    </script>
</body>
</html>'''
    
    # Write to file
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Đã tạo lại index.html")
    print(f"Tổng số file: {len(file_structure)}")
    print(f"Tổng số navigation items: {len(navigation)}")
    
    # Count by category
    from collections import Counter
    category_counts = Counter(item['category'] for item in navigation)
    print(f"\nPhân loại:")
    for category, count in sorted(category_counts.items()):
        print(f"   {category}: {count} file")

if __name__ == '__main__':
    main()
