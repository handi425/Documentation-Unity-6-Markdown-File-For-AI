[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-reference-other-files-from-uxml.html)
  * [中文](/cn/current/Manual/UIE-reference-other-files-from-uxml.html)
  * [日本語](/ja/current/Manual/UIE-reference-other-files-from-uxml.html)
  * [한국어](/kr/current/Manual/UIE-reference-other-files-from-uxml.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-reference-other-files-from-uxml.html)
  * [中文](/cn/current/Manual/UIE-reference-other-files-from-uxml.html)
  * [日本語](/ja/current/Manual/UIE-reference-other-files-from-uxml.html)
  * [한국어](/kr/current/Manual/UIE-reference-other-files-from-uxml.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [Structure UI with UXML](UIE-UXML.html)
  * Reference other files from UXML

[](UIE-reuse-uxml-files.html)

Reuse UXML files

[](UIE-manage-asset-reference.html)

Load UXML and USS C# scripts

# Reference other files from UXML

In a UXML file, you can use the `<Template>` and the `<Style>` elements to
reference other UXML or USS files. The two elements both accept either an
`src` attribute or a `path` attribute.

## The `src` attribute

Use the following syntax for the src attribute:

    
    
    src="<path-to-file>/<file-name-with-extension>"
    

Any errors during import, such as missing files, trigger an error message.

You can use a relative or an absolute path:

  * Absolute paths start from the project’s `Assets` folder and begin with a `/` or `project://database/`. For example, `/Assets/myFolder/myFile.uss` or `project://database/Assets/myFolder/myFile.uss`.
  * Relative paths start from the current file and exclude the `/`. For example, `../myFolder/myFile.uss`.

**Note** : To reference a file from packages, use the absolute path of the
package file that starts from the `Packages` folder. For example,
`/Packages/com.unity.package.name/file-name.uss` or
`project://database/Packages/com.unity.package.name/file-name.uss`. you must
use the format of `com.unity.package.name` rather than `package name` for the
package name.

## The `path` attribute

The `path` attribute uses the Unity Resources mechanisms, but doesn’t offer
error reporting at import time and doesn’t allow relative paths.

The `path` attribute accepts files located in either the `Resources` folder or
the `Editor Default Resources` folder, with the following rules:

  * If the file is in the `Resources` folder, don’t include the file extension. For example, write `path="template"` for a file located at `Assets/Resources/template.uxml`.
  * If the file is in the `Editor Default Resources` folder, you must include the file extension. For example, write `path="template.uxml"` for a file located at `Assets/Editor Default Resources/template.uxml`.

## Additional resources

  * [Add styles to UXML](UIE-add-style-to-uxml.html)
  * [Reuse UXML files](UIE-reuse-uxml-files.html)

[](UIE-reuse-uxml-files.html)

Reuse UXML files

[](UIE-manage-asset-reference.html)

Load UXML and USS C# scripts

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

