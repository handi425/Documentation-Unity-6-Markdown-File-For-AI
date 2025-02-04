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

# BuildPlayerOptions

struct in UnityEditor

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

Provide various options to control the behavior of
[BuildPipeline.BuildPlayer](BuildPipeline.BuildPlayer.html).

Additional resources: [EditorBuildSettings](EditorBuildSettings.html),
[BuildPlayerWindow.DefaultBuildMethods.GetBuildPlayerOptions](BuildPlayerWindow.DefaultBuildMethods.GetBuildPlayerOptions.html)

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class BuildPlayerOptionsExample
    {
        [[MenuItem](MenuItem.html)("Build/Log Build [Settings](CameraEditor.Settings.html)")]
        public static void MyBuild()
        {
            // Log some of the current build options retrieved from the Build [Settings](CameraEditor.Settings.html) Window
            [BuildPlayerOptions](BuildPlayerOptions.html) buildPlayerOptions = [BuildPlayerWindow.DefaultBuildMethods.GetBuildPlayerOptions](BuildPlayerWindow.DefaultBuildMethods.GetBuildPlayerOptions.html)(new [BuildPlayerOptions](BuildPlayerOptions.html)());
            [Debug.Log](Debug.Log.html)("[BuildPlayerOptions](BuildPlayerOptions.html)\n"
                + "Scenes: " + string.Join(",", buildPlayerOptions.scenes) + "\n"
                + "Build location: " + buildPlayerOptions.locationPathName + "\n"
                + "[Options](Progress.Options.html): " + buildPlayerOptions.options + "\n"
                + "[Target](GraphicsBuffer.Target.html): " + buildPlayerOptions.target);
        }
    }
    

### Properties

[assetBundleManifestPath](BuildPlayerOptions-assetBundleManifestPath.html)|
The path to an manifest file describing all of the asset bundles used in the
build (optional).  
---|---  
[extraScriptingDefines](BuildPlayerOptions-extraScriptingDefines.html)| The
additional preprocessor defines you can specify while compiling assemblies for
the Player. These defines are appended to the existing Scripting Define
Symbols list configured in the Player settings.  
[locationPathName](BuildPlayerOptions-locationPathName.html)| The path where
the application will be built.  
[options](BuildPlayerOptions-options.html)| Additional BuildOptions, like
whether to run the built player.  
[scenes](BuildPlayerOptions-scenes.html)| The Scenes to be included in the
build.  
[subtarget](BuildPlayerOptions-subtarget.html)| The Subtarget to build.  
[target](BuildPlayerOptions-target.html)| The BuildTarget to build.  
[targetGroup](BuildPlayerOptions-targetGroup.html)| The BuildTargetGroup to
build.  
  
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

