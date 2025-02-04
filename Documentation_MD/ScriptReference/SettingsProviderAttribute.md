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

# SettingsProviderAttribute

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

Attribute used to register a new [SettingsProvider](SettingsProvider.html).
Use this attribute to decorate a function that returns an instance of a
[SettingsProvider](SettingsProvider.html). If the function returns null, no
SettingsProvider appears in the Settings window.

    
    
    using System.IO;
    using System.Linq;
    using [UnityEditor](UnityEditor.html);  
      
    class MyCustomSettingsProvider : [SettingsProvider](SettingsProvider.html)
    {
        const string k_MyCustomSettingsPath = "[Resources](Resources.html)/MyCustomSettings.asset";
        public MyCustomSettingsProvider(string path, [SettingsScope](SettingsScope.html) scope)
            : base(path, scope) {}  
      
        public static bool IsSettingsAvailable()
        {
            return [File.Exists](Windows.File.Exists.html)(k_MyCustomSettingsPath);
        }  
      
        [[SettingsProvider](SettingsProvider.html)]
        public static [SettingsProvider](SettingsProvider.html) CreateMyCustomSettingsProvider()
        {
            if (IsSettingsAvailable())
            {
                return new MyCustomSettingsProvider("MyCustomSettings", [SettingsScope.Project](SettingsScope.Project.html));
            }  
      
            // [Settings](CameraEditor.Settings.html) [Asset](VersionControl.Asset.html) doesn't exist yet. No need to display anything in the [Settings](CameraEditor.Settings.html) window.
            return null;
        }
    }
    

### Constructors

[SettingsProviderAttribute](SettingsProviderAttribute-ctor.html)| Creates a
new SettingsProviderAttribute used to register new SettingsProvider.  
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

