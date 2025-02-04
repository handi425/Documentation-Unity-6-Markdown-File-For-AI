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

# AndroidProjectFilesModifier

class in UnityEditor.Android

Leave feedback

  

Implements interfaces:[IOrderedCallback](Build.IOrderedCallback.html)

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

An abstract class that contains methods to modify custom Android Gradle
project files during the build process.

**Note** : You can use this class to modify the Gradle project files that you
set up in the modules other than the default `unityLibrary` and `launcher`
Android Gradle modules. If you use this class to modify the contents of
Android Gradle project files in the default modules, the build will fail.  
  
This abstract class contains two callback methods: `Setup` and
`OnModifyAndroidProjectFiles`. Unity calls `Setup` before the build begins and
this method sets prerequisites for the build system. Unity calls
`OnModifyAndroidProjectFiles` after it creates the Gradle project, which means
all modifications you make in this method are applied directly to that
project.  
  
The generated files use Groovy syntax and all string-type properties use
double quotes.  
  
If your `OnModifyAndroidProjectFiles` callback depends on other files in the
project (or on the local machine), or if you want the callback to produce new
files, you must give this information to the build system in advance using
`Setup`. The incremental build pipeline requires this information to know what
files this callback produces and which files the callback depends on. This is
so the build pipeline can identify when this step needs to run and when it can
be skipped. The `Setup` method returns
[AndroidProjectFilesModifierContext](Android.AndroidProjectFilesModifierContext.html).
For more information, refer to
[AndroidProjectFilesModifierContext](Android.AndroidProjectFilesModifierContext.html).  
  
For information on when Unity invokes methods in this class, refer to [How
Unity builds Android applications](../Manual/how-unity-builds-android-
applications.html).  
  
In the `Setup` method, you can specify paths to the Gradle files that you want
to create in your custom Gradle module. The following example demonstrates how
you can specify these paths for the custom module `mycustommodule` and modify
the values in `build.gradle` and `AndroidManifest.xml` files.

    
    
    using System.IO;
    using UnityEditor.Android;
    using [Unity.Android.Gradle](Unity.Android.Gradle.html);  
      
    public class ModifyProjectScript : [AndroidProjectFilesModifier](Android.AndroidProjectFilesModifier.html)
    {
        public override [AndroidProjectFilesModifierContext](Android.AndroidProjectFilesModifierContext.html) Setup()
        {
            var ctx = new [AndroidProjectFilesModifierContext](Android.AndroidProjectFilesModifierContext.html)();
            ctx.Outputs.AddBuildGradleFile("mycustommodule/build.gradle");
            ctx.Outputs.AddManifestFile("mycustommodule/src/main/AndroidManifest.xml");
            return ctx;
        }  
      
        public override void OnModifyAndroidProjectFiles([AndroidProjectFiles](Android.AndroidProjectFiles.html) projectFiles)
        {
            var customGradleFile = new [ModuleBuildGradleFile](Unity.Android.Gradle.ModuleBuildGradleFile.html)();
            customGradleFile.Android.DefaultConfig.MinSdk.Set(28);
            projectFiles.SetBuildGradleFile("mycustommodule/build.gradle", customGradleFile);  
      
            var customManifestFile = new [AndroidManifestFile](Unity.Android.Gradle.Manifest.AndroidManifestFile.html)();
            customManifestFile.Manifest.Application.AddActivity("MyCustomActivity"); ;
            projectFiles.SetManifestFile("mycustommodule/src/main/AndroidManifest.xml", customManifestFile);
        }
    }
    

### Properties

[callbackOrder](Android.AndroidProjectFilesModifier-callbackOrder.html)|
Callback order when there are multiple implementations of
AndroidProjectFilesModifier.  
---|---  
  
### Public Methods

[OnModifyAndroidProjectFiles](Android.AndroidProjectFilesModifier.OnModifyAndroidProjectFiles.html)|
A callback for modifying files in the Android Gradle project after Unity
Editor creates it.  
---|---  
[Setup](Android.AndroidProjectFilesModifier.Setup.html)| A callback for
setting up prerequisites for modifying custom Android Gradle project files.  
  
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

