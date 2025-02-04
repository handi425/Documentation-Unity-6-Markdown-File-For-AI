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

#  [SettingsProvider](SettingsProvider.html).label

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

public string label;

### Description

Gets or sets the display name of the SettingsProvider as it appears in the
Settings window. If not set, the Settings window uses last token of
[SettingsProvider.settingsPath](SettingsProvider-settingsPath.html) instead.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEngine.UIElements;  
      
    class SettingsProviderExamples
    {
        void CreateVariousSettingsProviders()
        {
            // New Project setting that appears in its own root section (MyOwnSection) and not grouped under all the core settings.
            var p = new [SettingsProvider](SettingsProvider.html)("MyOwnSection/MySettings", [SettingsScope.Project](SettingsScope.Project.html));
            // here p.label == "MySettings"  
      
            // First parameter is a unique id used to place the [Settings](CameraEditor.Settings.html) in the tree view.
            // If a label is specified, this becomes the display name of the [SettingsProvider](SettingsProvider.html).
            var p2 = new [SettingsProvider](SettingsProvider.html)("MyOwnSection/MySettingsOfDoom", [SettingsScope.Project](SettingsScope.Project.html))
            {
                label = "A more proper [Settings](CameraEditor.Settings.html) Name"
            };  
      
            // Second parameter is the [Scope](Experimental.GraphView.Scope.html) of the [SettingsProvider](SettingsProvider.html). It determines whether this [SettingsProvider](SettingsProvider.html) appears in the
            // [Settings](CameraEditor.Settings.html) window (used for Project settings specified with [SettingsScope.Project](SettingsScope.Project.html))
            // or if it appears in the Preferences window (when specified with [SettingsScope.User](SettingsScope.User.html))
            var p3 = new [SettingsProvider](SettingsProvider.html)("Preferences/Multi touch", [SettingsScope.User](SettingsScope.User.html));
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

