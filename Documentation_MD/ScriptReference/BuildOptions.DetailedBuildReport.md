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

#  [BuildOptions](BuildOptions.html).DetailedBuildReport

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

Generates more information in the BuildReport.

The BuildReport object returned by BuildPipeline.BuildPlayer will contain more
details (about build times and contents), at the cost of a slightly
(typically, a few percents) longer build time.  
  
The following script example illustrates how to use
[DetailedBuildReport](BuildOptions.DetailedBuildReport.html) when building a
player. Create a project and add the script under Assets/Editor.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class DetailedBuildReportExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("Build/DetailedBuildReport example")]
        public static void MyBuild()
        {
            [BuildPlayerOptions](BuildPlayerOptions.html) buildPlayerOptions = new [BuildPlayerOptions](BuildPlayerOptions.html)();
            buildPlayerOptions.scenes = new[] { "Assets/scene.unity" };
            buildPlayerOptions.locationPathName = "DetailedReportBuild/MyGame.exe";
            buildPlayerOptions.target = [BuildTarget.StandaloneWindows64](BuildTarget.StandaloneWindows64.html);  
      
            buildPlayerOptions.options = [BuildOptions.DetailedBuildReport](BuildOptions.DetailedBuildReport.html);  
      
            var buildReport = [BuildPipeline.BuildPlayer](BuildPipeline.BuildPlayer.html)(buildPlayerOptions);
        }
    }
    

Now run the "Build/DetailedBuildReport example" scripts example.  
You can now get more information about the build process in the variable
"buildReport", that you can process using the
[BuildReport](Build.Reporting.BuildReport.html) API.  
You can find illustrations of how to query the
[BuildReport](Build.Reporting.BuildReport.html) API by looking at the [Build
Report Inspector source script ](https://github.com/Unity-
Technologies/BuildReportInspector).

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

