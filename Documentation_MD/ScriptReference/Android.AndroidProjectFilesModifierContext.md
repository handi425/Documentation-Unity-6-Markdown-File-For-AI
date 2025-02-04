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

# AndroidProjectFilesModifierContext

class in UnityEditor.Android

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

Represents a container that specifies additional dependencies and additional
outputs for `AndroidProjectFilesModifier`.

    
    
    using System.IO;
    using [Unity.Android.Gradle](Unity.Android.Gradle.html);
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Android;
    using UnityEngine;  
      
    public class ModifyProjectScript : [AndroidProjectFilesModifier](Android.AndroidProjectFilesModifier.html)
    {
        private string _myLibBuildGradle = Path.Combine("unityLibrary", "customPlugin", "build.gradle");
        public override [AndroidProjectFilesModifierContext](Android.AndroidProjectFilesModifierContext.html) Setup()
        {
            var projectFilesContext = new [AndroidProjectFilesModifierContext](Android.AndroidProjectFilesModifierContext.html)();
            // Tell the build system to expect a file to be produced in <gradleProject>/unityLibrary/customPlugin/build.gradle
            projectFilesContext.Outputs.AddBuildGradleFile(_myLibBuildGradle);  
      
            // Tell the build system that it should run OnModifyAndroidProjectFiles if MyConfig.json has changes since the last build
            projectFilesContext.Dependencies.DependencyFiles = new[]
            {
                "Assets/MyConfig.json"
            };  
      
            // Tell the build system to copy the directory to the Gradle project
            projectFilesContext.AddDirectoryToCopy("Assets/DirectoryToCopy", "destinationName");  
      
            // [Pass](ShaderData.Pass.html) some data/properties from the [Editor](Editor.html) to the OnModifyAndroidProjectFiles callback
            projectFilesContext.SetData("companyName", [PlayerSettings.companyName](PlayerSettings-companyName.html));
            // [Data](Unity.Android.Gradle.Manifest.Data.html) can be any serializable object
            projectFilesContext.SetData<[Vector2](Vector2.html)>("cursorHotspot", [PlayerSettings.cursorHotspot](PlayerSettings-cursorHotspot.html));  
      
            return projectFilesContext;
        }  
      
        public override void OnModifyAndroidProjectFiles([AndroidProjectFiles](Android.AndroidProjectFiles.html) projectFiles)
        {
            // Produce an object that will be serialized to <gradleProject>/unityLibrary/customPlugin/build.gradle
            var buildGradleFile = new [ModuleBuildGradleFile](Unity.Android.Gradle.ModuleBuildGradleFile.html)();
            buildGradleFile.Android.AndroidResources.NoCompress.Set(new []{"someValue"});
            // Set the object that will be serialized to <gradleProject>/unityLibrary/customPlugin/build.gradle
            projectFiles.SetBuildGradleFile(_myLibBuildGradle, buildGradleFile);  
      
            // Do some changes based on MyConfig.json here
            // ...  
      
            // Get the data/properties that were declare in Setup
            var companyName = projectFiles.GetData("companyName");
            var cursorHotspot = projectFiles.GetData<[Vector2](Vector2.html)>("cursorHotspot");
            // Do something based on the data
            // ...
        }
    }
    

### Properties

[Dependencies](Android.AndroidProjectFilesModifierContext.Dependencies.html)|
Represents a container that you can use to specify additional dependencies for
the AndroidProjectFilesModifier process depends.  
---|---  
[Outputs](Android.AndroidProjectFilesModifierContext.Outputs.html)| Represents
a container that you can use to specify additional files that will be created
in AndroidProjectFilesModifier.OnModifyAndroidProjectFiles.  
  
### Constructors

[AndroidProjectFilesModifierContext](Android.AndroidProjectFilesModifierContext-
ctor.html)| Container constructor.  
---|---  
  
### Public Methods

[AddDirectoryAsGuidToCopy](Android.AndroidProjectFilesModifierContext.AddDirectoryAsGuidToCopy.html)|
Declare a directory to copy into the Gradle project.  
---|---  
[AddDirectoryToCopy](Android.AndroidProjectFilesModifierContext.AddDirectoryToCopy.html)|
Declare a directory to copy into the Gradle project.  
[AddFileAsGuidToCopy](Android.AndroidProjectFilesModifierContext.AddFileAsGuidToCopy.html)|
Declare an asset to copy into the Gradle project.  
[AddFileToCopy](Android.AndroidProjectFilesModifierContext.AddFileToCopy.html)|
Declare a file to copy into the Gradle project.  
[SetData](Android.AndroidProjectFilesModifierContext.SetData.html)| Sets data
for the OnModifyAndroidProjectFiles callback.  
  
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

