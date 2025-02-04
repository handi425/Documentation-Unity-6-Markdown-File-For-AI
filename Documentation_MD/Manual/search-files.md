[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/search-files.html)
  * [中文](/cn/current/Manual/search-files.html)
  * [日本語](/ja/current/Manual/search-files.html)
  * [한국어](/kr/current/Manual/search-files.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/search-files.html)
  * [中文](/cn/current/Manual/search-files.html)
  * [日本語](/ja/current/Manual/search-files.html)
  * [한국어](/kr/current/Manual/search-files.html)

  * [The Unity Editor](unity-editor.html)
  * [Unity Search](search-overview.html)
  * [Search Providers](search-providers.html)
  * Search for files

[](search-calculator.html)

The calculator

[](search-api.html)

Execute API methods

# Search for files

The File Search Provider searches the file system to find files that match a
specific pattern.

**NOTE:** This search requires a search token to execute it. You cannot make
it an [active Search Provider](search-filters.html#persistent-search-filters),
or combine it with other Search Providers.

**[Search token](search-filters.html#search-tokens):** `find:`

**[Default action](search-usage.html#default-actions):** Select the file.

**[Context menu actions](search-usage.html#additional-actions):**

Action | Function  
---|---  
**Select** | Selects the file in the **Project** window.  
**Open:** | Opens the file, either in Unity or an external editor.  
**Delete:** | Deletes the file.  
**Copy Path** | Copies the path of the file.  
**Reimport** | Reimports the file.  
**Reveal** | Selects the file in the operating system’s file browser.  
**Properties** | Opens the file’s property settings.  
  
Your search query can contain a C# regex to perform matching or glob
expressions with the following wildcards. A glob expression is converted to a
normal regex using the equivalency described in the table below:

Glob wildcards | Description | Example | Matches | Does not match | Equivalent regex  
---|---|---|---|---|---  
* | Matches any number of any characters including none | Law* | Law, Laws, Lawyer | Groklaw, La, aw | .*  
. | Matches any single character including none | Law. | Law, Laws | La, aw | .  
  
![asset filter](../uploads/Main/search-provider-file.png)  
_File Search Provider_

[](search-calculator.html)

The calculator

[](search-api.html)

Execute API methods

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

