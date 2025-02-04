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

# BuildReport

class in UnityEditor.Build.Reporting

/

Inherits from:[Object](Object.html)

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

The BuildReport API gives you information about the Unity build process.

A BuildReport object is returned by
[BuildPipeline.BuildPlayer](BuildPipeline.BuildPlayer.html) and can be used to
discover information about the files output, the build steps taken, and other
platform-specific information such as native code stripping.  
  
For AssetBundle builds the BuildReport is available by calling
[GetLatestReport](Build.Reporting.BuildReport.GetLatestReport.html)
immediately after calling
[BuildPipeline.BuildAssetBundles](BuildPipeline.BuildAssetBundles.html).

    
    
    using System.IO;
    using System.Linq;
    using System.Text;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Build;
    using UnityEditor.Build.Reporting;
    using UnityEngine;  
      
    public class BuildReportExample
    {
        [[MenuItem](MenuItem.html)("Example/Build [AssetBundle](AssetBundle.html)")]
        static public void BuildBundles()
        {
            string buildOutputDirectory = "BuildOutput";
            if (![Directory.Exists](Windows.Directory.Exists.html)(buildOutputDirectory))
                [Directory.CreateDirectory](Windows.Directory.CreateDirectory.html)(buildOutputDirectory);  
      
            var bundleDefinitions = new [AssetBundleBuild](AssetBundleBuild.html)[]
            {
                new [AssetBundleBuild](AssetBundleBuild.html)()
                {
                    assetBundleName = "MyBundle",
                    assetNames = new string[] { "Assets/Scenes/SampleScene.unity" }
                }
            };  
      
            [BuildPipeline.BuildAssetBundles](BuildPipeline.BuildAssetBundles.html)(
                buildOutputDirectory,
                bundleDefinitions,
                [BuildAssetBundleOptions.ForceRebuildAssetBundle](BuildAssetBundleOptions.ForceRebuildAssetBundle.html),
                [EditorUserBuildSettings.activeBuildTarget](EditorUserBuildSettings-activeBuildTarget.html));  
      
            [BuildReport](Build.Reporting.BuildReport.html) report = [BuildReport.GetLatestReport](Build.Reporting.BuildReport.GetLatestReport.html)();
            if (report != null)
            {
                var sb = new StringBuilder();
                sb.AppendLine("Build result   : " + report.summary.result);
                sb.AppendLine("Build size     : " + report.summary.totalSize + " bytes");
                sb.AppendLine("Build time     : " + report.summary.totalTime);
                sb.AppendLine("[Error](PackageManager.Error.html) summary  : " + report.SummarizeErrors());
                sb.Append(LogBuildReportSteps(report));
                sb.AppendLine(LogBuildMessages(report));
                [Debug.Log](Debug.Log.html)(sb.ToString());
            }
            else
            {
                // Certain errors like invalid input can fail the build immediately, with no [BuildReport](Build.Reporting.BuildReport.html) written
                [Debug.Log](Debug.Log.html)("[AssetBundle](AssetBundle.html) build failed");
            }
        }  
      
        public static string LogBuildReportSteps([BuildReport](Build.Reporting.BuildReport.html) buildReport)
        {
            var sb = new StringBuilder();  
      
            sb.AppendLine($"Build steps: {buildReport.steps.Length}");
            int maxWidth = buildReport.steps.Max(s => s.name.Length + s.depth) + 3;
            foreach (var step in buildReport.steps)
            {
                string rawStepOutput = new string('-', step.depth + 1) + ' ' + step.name;
                sb.AppendLine($"{rawStepOutput.PadRight(maxWidth)}: {step.duration:g}");
            }
            return sb.ToString();
        }  
      
        public static string LogBuildMessages([BuildReport](Build.Reporting.BuildReport.html) buildReport)
        {
            var sb = new StringBuilder();
            foreach (var step in buildReport.steps)
            {
                foreach (var message in step.messages)
                    // If desired, this logic could ignore any Info or Warning messages to focus on more serious messages
                    sb.AppendLine($"[{message.type}] {message.content}");
            }  
      
            string messages = sb.ToString();
            if (messages.Length > 0)
                return "Messages logged during Build:\n" + messages;
            else
                return "";
        }
    }  
      
    // For the purpose of demonstration, this callback logs different types of errors and forces a build failure
    [BuildCallbackVersion(1)]
    class MyTroublesomeBuildCallback : [IProcessSceneWithReport](Build.IProcessSceneWithReport.html)
    {
        public int callbackOrder { get { return 0; } }
        public void OnProcessScene(UnityEngine.SceneManagement.Scene scene, [BuildReport](Build.Reporting.BuildReport.html) report)
        {
            [Debug.Log](Debug.Log.html)("MyTroublesomeBuildCallback called for " + scene.name);
            [Debug.LogError](Debug.LogError.html)("Logging an error");  
      
            throw new [BuildFailedException](Build.BuildFailedException.html)("Forcing the build to stop");
        }
    }
    

### Properties

[packedAssets](Build.Reporting.BuildReport-packedAssets.html)| An array of all
the PackedAssets generated by the build process.  
---|---  
[scenesUsingAssets](Build.Reporting.BuildReport-scenesUsingAssets.html)| An
optional array of ScenesUsingAssets generated by the build process if
BuildOptions.DetailedBuildReport was used during the build.  
[steps](Build.Reporting.BuildReport-steps.html)| An array of all the
BuildSteps that took place during the build process.  
[strippingInfo](Build.Reporting.BuildReport-strippingInfo.html)| The
StrippingInfo object for the build.  
[summary](Build.Reporting.BuildReport-summary.html)| A BuildSummary containing
overall statistics and data about the build process.  
  
### Public Methods

[GetFiles](Build.Reporting.BuildReport.GetFiles.html)| Returns an array of all
the files output by the build process.  
---|---  
[SummarizeErrors](Build.Reporting.BuildReport.SummarizeErrors.html)| Returns a
string summarizing any errors that occurred during the build  
  
### Static Methods

[GetLatestReport](Build.Reporting.BuildReport.GetLatestReport.html)| Return
the build report generated by the most recent Player or AssetBundle build  
---|---  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

