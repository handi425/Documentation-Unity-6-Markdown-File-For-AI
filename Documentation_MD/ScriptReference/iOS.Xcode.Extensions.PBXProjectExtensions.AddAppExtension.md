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
[PBXProjectExtensions](iOS.Xcode.Extensions.PBXProjectExtensions.html).AddAppExtension

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
AddAppExtension([iOS.Xcode.PBXProject](iOS.Xcode.PBXProject.html) proj, string
mainTargetGuid, string name, string bundleId, string infoPlistPath);

### Parameters

proj | The implicit `this` parameter for the extension method.  
---|---  
mainTargetGuid | The GUID of the main target to link the app to.  
name | The name of the app extension.  
bundleId | The bundle ID of the app extension. The bundle ID must be prefixed with the parent app bundle ID.  
infoPlistPath | Path to the app extension Info.plist document.  
  
### Returns

**string** The GUID of the new target.

### Description

Creates an app extension.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEditor.iOS.Xcode;
    using UnityEditor.iOS.Xcode.Extensions;
    using System.IO;
    using UnityEditor.Callbacks;  
      
    public class ScriptBatch : [MonoBehaviour](MonoBehaviour.html)
    {
        [PostProcessBuild]
        private static void PostProcessBuild_iOS([BuildTarget](BuildTarget.html) target, string buildPath)
        {
            File.Copy("Assets/extension/TodayViewController.h", buildPath + "/appext/TodayViewController.h");
            File.Copy("Assets/extension/TodayViewController.m", buildPath + "/appext/TodayViewController.m");  
      
            [PBXProject](iOS.Xcode.PBXProject.html) proj = new [PBXProject](iOS.Xcode.PBXProject.html)();
            string projPath = [PBXProject.GetPBXProjectPath](iOS.Xcode.PBXProject.GetPBXProjectPath.html)(buildPath);
            proj.ReadFromFile(projPath);  
      
            string targetGuid = proj.GetUnityFrameworkTargetGuid();  
      
            string newTarget = proj.AddAppExtension(targetGuid, "appext", "com.unity3d.product.appext", "appext/Info.plist");
            proj.AddFileToBuild(newTarget, proj.AddFile(buildPath + "/appext/TodayViewController.h", "appext/TodayViewController.h"));
            proj.AddFileToBuild(newTarget, proj.AddFile(buildPath + "/appext/TodayViewController.m", "appext/TodayViewController.m"));
            proj.AddFrameworkToProject(newTarget, "NotificationCenter.framework", true);
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

