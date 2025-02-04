[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#  [BuildOptions](BuildOptions.html).SymlinkSources

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Symlink sources when generating the project. This is useful if you're changing
source files inside the generated project and want to bring the changes back
into your Unity project or a package.

This option affects sources in both Unity projects and packages.  
  
Only the following platforms support this option:  
  
**iOS** : When symlinkSources is enabled, Unity creates symlinks for libraries
(libil2cpp.a, libiPhone-lib.a, etc.). This means you don't need to copy the
libraries. Sources with .mm, .m, .cpp, .c, .h, .swift, and .xib extensions are
referenced externally from Xcode project.  
  
**Android** : When `symlinkSources` is enabled, Gradle project references
.java, .kt and .androidlib plug-in sources externally from Unity project
rather than copying the source files directly into the Gradle project. In case
of .androidlib plug-in, the plug-in folder must include `build.gradle` file
for the `symlinkSources` option to work.  
  
Additional resources:
[BuildPipeline.BuildPlayer](BuildPipeline.BuildPlayer.html),
[EditorUserBuildSettings.symlinkSources](EditorUserBuildSettings-
symlinkSources.html).

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

