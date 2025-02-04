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

#  [PBXProject](iOS.Xcode.PBXProject.html).AddCapability

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

public bool AddCapability(string targetGuid,
[iOS.Xcode.PBXCapabilityType](iOS.Xcode.PBXCapabilityType.html) capability,
string entitlementsFilePath, bool addOptionalFramework);

### Parameters

targetGuid | The GUID of the target, such as the one returned by [GetUnityFrameworkTargetGuid](iOS.Xcode.PBXProject.GetUnityFrameworkTargetGuid.html).  
---|---  
capability | The capability to enable.  
entitlementsFilePath | Path to the entitlements file to be used for this capability. Information regarding the contents of entitlements files can be found in [Apple Documentation](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/AboutEntitlements.html)  
addOptionalFramework | Set this to true to indicate that this capability requires additional frameworks. Set it to false if no additional frameworks are required.  
  
### Returns

**bool** True if the capability was successfully added.

### Description

Adds a target capability to the Xcode project.

This enables behavior based on the capability type. Some capabilities require
additional setup within Xcode. For more control over the specific settings of
capability, use the
[ProjectCapabilityManager](iOS.Xcode.ProjectCapabilityManager.html) class.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using System.IO;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Callbacks;
    using UnityEditor.iOS.Xcode;  
      
    public class Sample_AddCapability  
    {
        [PostProcessBuild]
        public static void OnPostprocessBuild([BuildTarget](BuildTarget.html) buildTarget, string pathToBuiltProject)
        {  
      
            // Stop processing if build target is not [iOS](PlayerSettings.iOS.html)
            if (buildTarget != [BuildTarget.iOS](BuildTarget.iOS.html))
                return;  
      
            // Initialize [PBXProject](iOS.Xcode.PBXProject.html)
            string projectPath = [PBXProject.GetPBXProjectPath](iOS.Xcode.PBXProject.GetPBXProjectPath.html)(pathToBuiltProject);  
      
            [PBXProject](iOS.Xcode.PBXProject.html) pbxProject = new [PBXProject](iOS.Xcode.PBXProject.html)();
            pbxProject.ReadFromFile(projectPath);  
      
            // Get GUIDs for UnityFramework and Main targets
            string mainTargetGuid = pbxProject.GetUnityMainTargetGuid();
            string unityFrameworkTargetGuid = pbxProject.GetUnityFrameworkTargetGuid();  
      
    
            // Create an entitlements file for your capability
            string entitlementsFileName = "Example.entitlements";  
      
            [PlistDocument](iOS.Xcode.PlistDocument.html) plistDocument = new [PlistDocument](iOS.Xcode.PlistDocument.html)();
            plistDocument.Create();  
      
            [PlistElementDict](iOS.Xcode.PlistElementDict.html) rootDict = plistDocument.root;
            rootDict.SetString("com.apple.developer.applesignin", "Default");  
      
            plistDocument.WriteToFile(Path.Combine(pathToBuiltProject, entitlementsFileName));  
      
            // Add 'Sign in with Apple' capability to the proejct with the entitlements file specified
            pbxProject.AddCapability(mainTargetGuid, [PBXCapabilityType.SignInWithApple](iOS.Xcode.PBXCapabilityType.SignInWithApple.html), entitlementsFileName);  
      
            // Apply changes to the pbxproj file
            pbxProject.WriteToFile(projectPath);
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

