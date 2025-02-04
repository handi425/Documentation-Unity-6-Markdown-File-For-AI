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

#  [OverlayCanvas](Overlays.OverlayCanvas.html).ShowPopup

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

public void ShowPopup();

## Declaration

public void ShowPopup([Vector2](Vector2.html) position);

### Parameters

position | The GUI position relative to the window.  
---|---  
  
### Description

Displays an overlay as a pop-up in a [EditorWindow](EditorWindow.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Overlays;
    using UnityEditor.ShortcutManagement;
    using UnityEngine;
    using UnityEngine.UIElements;
    
    class PopUpOnlyOverlay : [Overlay](Overlays.Overlay.html)
    {
        public PopUpOnlyOverlay()
        {
            displayName = "Pop Me Up";
        }
    
        public override [VisualElement](UIElements.VisualElement.html) CreatePanelContent()
        {
            return new [Label](UIElements.Label.html)("I'm a pop-up overlay!");
        }
    
        [Shortcut("PopUpOnlyOverlayExample/Pop Up [Overlay](Overlays.Overlay.html)",typeof([SceneView](SceneView.html)), [KeyCode.P](KeyCode.P.html), [ShortcutModifiers.Shift](ShortcutManagement.ShortcutModifiers.Shift.html))]
        static void ShowOverlay([ShortcutArguments](ShortcutManagement.ShortcutArguments.html) args)
        {
            var window = args.context as [EditorWindow](EditorWindow.html);
            if (window is [ISupportsOverlays](Overlays.ISupportsOverlays.html))
                window.overlayCanvas.ShowPopup<PopUpOnlyOverlay>();
        }
    }
    .

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

