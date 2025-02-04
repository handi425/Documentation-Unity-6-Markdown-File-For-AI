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

#  [BuildPipeline](BuildPipeline.html).BuildPlayer

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

## Declaration

public static [Build.Reporting.BuildReport](Build.Reporting.BuildReport.html)
BuildPlayer([BuildPlayerOptions](BuildPlayerOptions.html) buildPlayerOptions);

### Parameters

buildPlayerOptions | Provide various options to control the behavior of [BuildPipeline.BuildPlayer](BuildPipeline.BuildPlayer.html).  
---|---  
  
### Returns

**BuildReport** A [BuildReport](Build.Reporting.BuildReport.html) object
containing build process information.

### Description

Builds a player.

Use this function to programatically create a build of your project.  
  
Calling this method will invalidate any variables in the editor script that
reference GameObjects, so they will need to be reacquired after the call.  
  
Scripts can run at strategic points during the build by implementing one of
the supported callback interfaces, for example
[BuildPlayerProcessor](Build.BuildPlayerProcessor.html),
[IPreprocessBuildWithReport](Build.IPreprocessBuildWithReport.html),
[IProcessSceneWithReport](Build.IProcessSceneWithReport.html) and
[IPostprocessBuildWithReport](Build.IPostprocessBuildWithReport.html).  
  
Note: Be aware that changes to [scripting symbols](../Manual/platform-
dependent-compilation.html) only take effect at the next domain reload, when
scripts are recompiled.  
  
This means if you make changes to the defined scripting symbols via code using
PlayerSettings.SetDefineSymbolsForGroup without a domain reload before calling
this function, those changes won't take effect.  
  
It also means that the built-in scripting symbols defined for the current
active target platform (such as UNITY_STANDALONE_WIN, or UNITY_ANDROID) remain
in place even if you try to build for a different target platform, which can
result in the wrong code being compiled into your build.  
  
Additional resources:
[BuildPlayerWindow.DefaultBuildMethods.BuildPlayer](BuildPlayerWindow.DefaultBuildMethods.BuildPlayer.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEditor.Build.Reporting;  
      
    // Output the build size or a failure depending on BuildPlayer.  
      
    public class BuildPlayerExample
    {
        [[MenuItem](MenuItem.html)("Build/Build [iOS](PlayerSettings.iOS.html)")]
        public static void MyBuild()
        {
            [BuildPlayerOptions](BuildPlayerOptions.html) buildPlayerOptions = new [BuildPlayerOptions](BuildPlayerOptions.html)();
            buildPlayerOptions.scenes = new[] { "Assets/Scene1.unity", "Assets/Scene2.unity" };
            buildPlayerOptions.locationPathName = "iOSBuild";
            buildPlayerOptions.target = [BuildTarget.iOS](BuildTarget.iOS.html);
            buildPlayerOptions.options = [BuildOptions.None](BuildOptions.None.html);  
      
            [BuildReport](Build.Reporting.BuildReport.html) report = [BuildPipeline.BuildPlayer](BuildPipeline.BuildPlayer.html)(buildPlayerOptions);
            [BuildSummary](Build.Reporting.BuildSummary.html) summary = report.summary;  
      
            if (summary.result == [BuildResult.Succeeded](Build.Reporting.BuildResult.Succeeded.html))
            {
                [Debug.Log](Debug.Log.html)("Build succeeded: " + summary.totalSize + " bytes");
            }  
      
            if (summary.result == [BuildResult.Failed](Build.Reporting.BuildResult.Failed.html))
            {
                [Debug.Log](Debug.Log.html)("Build failed");
            }
        }
    }
    

* * *

## Declaration

public static [Build.Reporting.BuildReport](Build.Reporting.BuildReport.html)
BuildPlayer([BuildPlayerWithProfileOptions](BuildPlayerWithProfileOptions.html)
buildPlayerWithProfileOptions);

### Parameters

buildPlayerWithProfileOptions | Provide various options to control the behavior of [BuildPipeline.BuildPlayer](BuildPipeline.BuildPlayer.html) when using a build profile.  
---|---  
  
### Returns

**BuildReport** A [BuildReport](Build.Reporting.BuildReport.html) object
containing build process information.

### Description

Builds a player from a specific build profile.

* * *

## Declaration

public static [Build.Reporting.BuildReport](Build.Reporting.BuildReport.html)
BuildPlayer(string[] levels, string locationPathName,
[BuildTarget](BuildTarget.html) target, [BuildOptions](BuildOptions.html)
options);

## Declaration

public static [Build.Reporting.BuildReport](Build.Reporting.BuildReport.html)
BuildPlayer(EditorBuildSettingsScene[] levels, string locationPathName,
[BuildTarget](BuildTarget.html) target, [BuildOptions](BuildOptions.html)
options);

### Parameters

levels | The scenes to include in the build. If empty, the build includes only the current open scene. Paths are relative to the project folder, for example `Assets/MyLevels/MyScene.unity`.  
---|---  
locationPathName | The path where the application will be built. For information on the platform extensions to include in the path, refer to [Build path requirements for target platforms](../Manual/build-path-requirements.html).  
target | The [BuildTarget](BuildTarget.html) to build.  
options | Additional [BuildOptions](BuildOptions.html), like whether to run the built player.  
  
### Returns

**BuildReport** A [BuildReport](Build.Reporting.BuildReport.html) object
containing build process information.

### Description

Builds a Player. These overloads are still supported, but will be replaced.
Please use BuildPlayer([BuildPlayerOptions](BuildPlayerOptions.html)
buildPlayerOptions) and
BuildPlayer([BuildPlayerWithProfileOptions](BuildPlayerWithProfileOptions.html)
buildPlayerWithProfileOptions) instead.

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

