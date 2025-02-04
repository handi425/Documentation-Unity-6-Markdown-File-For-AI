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

# LightingWindowTab

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

Base class to add custom tabs to the Lighting window.

See also
[LightingWindowEnvironmentSection](LightingWindowEnvironmentSection.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Rendering;
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    class CustomLightingTab : [LightingWindowTab](LightingWindowTab.html)
    {
        public override void OnEnable()
        {
            titleContent = new [GUIContent](GUIContent.html)("Custom");
            priority = 1; // This tab will be the second option in the toolbar
        }  
      
        public override void OnGUI()
        {
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("My Custom Lighting [Tab](UIElements.Tab.html) !!");
        }
    }
    

In this example, a new section is added in the Lighting window with the name
Custom.

### Properties

[priority](LightingWindowTab-priority.html)| The priority of the tab in the
header toolbar.  
---|---  
[titleContent](LightingWindowTab-titleContent.html)| The title of the tab.  
  
### Public Methods

[FocusTab](LightingWindowTab.FocusTab.html)| FocusTab will open the lighting
window with this tab selected.  
---|---  
[HasHelpGUI](LightingWindowTab.HasHelpGUI.html)| Returns true if window has a
doc button in the header.  
[OnBakeButtonGUI](LightingWindowTab.OnBakeButtonGUI.html)| OnBakeButtonGUI is
called to draw a button at the bottom of the tab.  
[OnDisable](LightingWindowTab.OnDisable.html)| OnDisable is called when this
Inspector override is not used anymore.  
[OnEnable](LightingWindowTab.OnEnable.html)| OnEnable is called when this
Inspector override is used.  
[OnGUI](LightingWindowTab.OnGUI.html)| A callback that is called when drawing
the main section of the tab.  
[OnHeaderSettingsGUI](LightingWindowTab.OnHeaderSettingsGUI.html)| A callback
that is called when drawing the header icons in the top right of the tab.  
[OnSelectionChange](LightingWindowTab.OnSelectionChange.html)| Called when the
selection changes.  
[OnSummaryGUI](LightingWindowTab.OnSummaryGUI.html)| A callback that is called
when drawing the bottom section of the tab.  
  
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

