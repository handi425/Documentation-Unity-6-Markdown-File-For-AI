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
[PBXProjectExtensions](iOS.Xcode.Extensions.PBXProjectExtensions.html).AddWatchApp

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

public static string
AddWatchApp([iOS.Xcode.PBXProject](iOS.Xcode.PBXProject.html) proj, string
mainTargetGuid, string watchExtensionTargetGuid, string name, string bundleId,
string infoPlistPath);

### Parameters

proj | The implicit `this` parameter for the extension method.  
---|---  
mainTargetGuid | The GUID of the main target to link the watch extension to.  
watchExtensionTargetGuid | The GUID of watch extension as returned by [[AddWatchExtension()]].  
name | The name of the watch app. It must the same as the name of the watch extension.  
bundleId | The bundle ID of the watch app.  
infoPlistPath | Path to the watch app Info.plist document.  
  
### Returns

**string** The GUID of the new target.

### Description

Creates a watch application.

    
    
    using System.Collections.Generic;
    using System.IO;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Callbacks;
    using UnityEditor.iOS.Xcode;
    using UnityEditor.iOS.Xcode.Extensions;
    using UnityEngine;  
      
    public class SetupWatchExtension
    {
        [PostProcessBuild]
        private static void PostProcessBuild_iOS([BuildTarget](BuildTarget.html) target, string buildPath)
        {
            [PBXProject](iOS.Xcode.PBXProject.html) proj = new [PBXProject](iOS.Xcode.PBXProject.html)();
            string projPath = [PBXProject.GetPBXProjectPath](iOS.Xcode.PBXProject.GetPBXProjectPath.html)(buildPath);
            proj.ReadFromFile(projPath);
            string targetGuid = proj.GetUnityFrameworkTargetGuid();
            string watchExtensionTargetGuid = [PBXProjectExtensions.AddWatchExtension](iOS.Xcode.Extensions.PBXProjectExtensions.AddWatchExtension.html)(proj, targetGuid, "watchtest Extension",
                "com.unity3d.watchtest.watchkitapp.watchkitextension",
                "watchtest Extension/Info.plist");
            string watchAppTargetGuid = [PBXProjectExtensions.AddWatchApp](iOS.Xcode.Extensions.PBXProjectExtensions.AddWatchApp.html)(proj, targetGuid, watchExtensionTargetGuid,
                "watchtest", "com.unity3d.watchtest.watchkitapp", "watchtest/Info.plist");  
      
            [FileUtil.CopyFileOrDirectory](FileUtil.CopyFileOrDirectory.html)("Assets/[Plugins](Unity.Android.Gradle.Plugins.html)/iOSWatchAppFiles/watchtest", Path.Combine(buildPath, "watchtest"));
            [FileUtil.CopyFileOrDirectory](FileUtil.CopyFileOrDirectory.html)("Assets/[Plugins](Unity.Android.Gradle.Plugins.html)/iOSWatchAppFiles/watchtest Extension", Path.Combine(buildPath, "watchtest Extension"));  
      
            var filesToBuild = new List<string>
            {
                "watchtest/Interface.storyboard",
                "watchtest/Assets.xcassets",
            };  
      
            foreach (var path in filesToBuild)
            {
                var fileGuid = proj.AddFile(path, path);
                proj.AddFileToBuild(watchAppTargetGuid, fileGuid);
            }  
      
            filesToBuild = new List<string>
            {
                "watchtest Extension/Assets.xcassets",  
      
                "watchtest Extension/ExtensionDelegate.h",
                "watchtest Extension/ExtensionDelegate.m",
                "watchtest Extension/InterfaceController.h",
                "watchtest Extension/InterfaceController.m",
                "watchtest Extension/NotificationController.h",
                "watchtest Extension/NotificationController.m",
            };  
      
            foreach (var path in filesToBuild)
            {
                var fileGuid = proj.AddFile(path, path);
                proj.AddFileToBuild(watchExtensionTargetGuid, fileGuid);
            }  
      
            var filesToAdd = new List<string>
            {
                "watchtest/Info.plist",
                "watchtest Extension/PushNotificationPayload.apns",
                "watchtest Extension/Info.plist",
            };  
      
            foreach (var path in filesToAdd)
                proj.AddFile(path, path);  
      
            proj.WriteToFile(projPath);
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

