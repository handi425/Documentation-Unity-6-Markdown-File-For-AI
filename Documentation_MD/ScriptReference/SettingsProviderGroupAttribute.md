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

# SettingsProviderGroupAttribute

class in UnityEditor

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

Attribute used to register multiple [SettingsProvider](SettingsProvider.html)
items. Use this attribute to decorate a function that returns an array of
[SettingsProvider](SettingsProvider.html) instances. If the function returns
null, no SettingsProvider appears in the Settings window.

    
    
    using System.IO;
    using System.Linq;
    using [UnityEditor](UnityEditor.html);  
      
    class [XRSettings](XR.XRSettings.html) : [SettingsProvider](SettingsProvider.html)
    {
        const string k_XRSettingsFolder = "Assets/[Editor](Editor.html)/[XRSettings](XR.XRSettings.html)";
        public [XRSettings](XR.XRSettings.html)(string path, [SettingsScope](SettingsScope.html) scope = [SettingsScope.Project](SettingsScope.Project.html))
            : base(path, scope)
        {
        }  
      
        [SettingsProviderGroup]
        public static [SettingsProvider](SettingsProvider.html)[] CreateProviders()
        {
            var files = Directory.GetFileSystemEntries(k_XRSettingsFolder, "*.json");
            return files.Select(entry =>
            {
                // First parameter is the path of the settings in the [Settings](CameraEditor.Settings.html) window.
                return new [XRSettings](XR.XRSettings.html)("Project/[XRSettings](XR.XRSettings.html)/" + Path.GetFileNameWithoutExtension(entry));
            }).ToArray();
        }
    }
    

### Constructors

[SettingsProviderGroupAttribute](SettingsProviderGroupAttribute-ctor.html)|
Creates a SettingsProviderGroupAttribute used to register multiple
SettingsProviders.  
---|---  
  
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

