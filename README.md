# Unity Documentation

This repository contains Unity's official documentation including Manual and Script Reference. This documentation helps developers understand how to use Unity Engine and its APIs.

## Directory Structure

```
.
├── Documentation_MD/         # Documentation in Markdown format
│   ├── Manual/             # Manual in MD format
│   └── ScriptReference/    # API Reference in MD format
├── Manual/                 # Manual in HTML format
├── ScriptReference/        # API Reference in HTML format
└── process_docs.py        # Script for processing documentation
```

## Content

### Manual
The manual contains comprehensive guides about:
- 2D and 3D Game Development
- Asset Management and Asset Bundles
- Platform Development (Android, iOS, etc.)
- Graphics and Rendering
- Animation System
- Physics
- And other Unity topics

### Script Reference
Contains complete API documentation for:
- Unity Classes and Components
- Methods and Properties
- Events and Callbacks
- Platform-specific APIs

## Format
Documentation is available in 2 formats:
1. **HTML** - Primary format that can be opened in browsers
2. **Markdown** - Alternative format that's easier to read in text editors

## Usage

1. To view the manual, open HTML files in the `Manual/` folder
2. To view API reference, open HTML files in the `ScriptReference/` folder
3. For markdown format, use the `Documentation_MD/` folder

## Processing
The `process_docs.py` file is used to process and transform documentation. Please refer to the comments within the script for usage details.

## Notes
- Make sure to use documentation version that matches your Unity version
- API references may differ between Unity versions
- Documentation in markdown format is still under development