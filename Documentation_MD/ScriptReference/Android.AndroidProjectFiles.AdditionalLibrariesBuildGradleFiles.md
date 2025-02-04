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

#
[AndroidProjectFiles](Android.AndroidProjectFiles.html).AdditionalLibrariesBuildGradleFiles

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

public IReadOnlyDictionary<string,ModuleBuildGradleFile>
AdditionalLibrariesBuildGradleFiles;

### Description

A representation of the `build.gradle` files that were added to plugins
(libraries) that didn't have a `build.gradle` file.

Files are located in `unityLibrary/{pluginName}/build.gradle`.  
  
If you have a plugin called `myLibrary` that doesn't contain `build.gradle`
file, the file will be generated and placed in
`unityLibrary/mylibrary.androidlib/build.gradle`. You can use this path to
access the file object in this dictionary.

    
    
    using System.IO;
    using UnityEditor.Android;
    using [Unity.Android.Gradle](Unity.Android.Gradle.html);  
      
    public class ModifyProjectScript : [AndroidProjectFilesModifier](Android.AndroidProjectFilesModifier.html)
    {
        public override void OnModifyAndroidProjectFiles([AndroidProjectFiles](Android.AndroidProjectFiles.html) projectFiles)
        {
            // Add a Google() repository to a build.gradle file in mylibrary.androidlib library
            var myLibraryBuildGradle = projectFiles.AdditionalLibrariesBuildGradleFiles[Path.Combine("unityLibrary", "mylibrary.androidlib", "build.gradle")];
            myLibraryBuildGradle.Repositories.AddRepository([Repositories.Google](Unity.Android.Gradle.Repositories.Google.html));
        }
    }
    

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

