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

# DockZone

enumeration

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

DockZone describes the area of the screen that an
[Overlay](Overlays.Overlay.html) is displayed in.

Use [DockZone](Overlays.DockZone.html) in an
[OverlayAttribute](Overlays.OverlayAttribute.html) to set the default location
for an [Overlay](Overlays.Overlay.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Overlays;
    using UnityEngine;
    using UnityEngine.UIElements;  
      
    // Use [OverlayAttribute](Overlays.OverlayAttribute.html) to specify that in new [Scene](SceneManagement.Scene.html) Views, when this [Overlay](Overlays.Overlay.html) is first opened it will be in the
    // top toolbar, aligned to the left side.
    [[Overlay](Overlays.Overlay.html)(typeof([SceneView](SceneView.html)), "Docked Top [Toolbar](UIElements.Toolbar.html), Left Aligned", defaultDockZone = [DockZone.TopToolbar](Overlays.DockZone.TopToolbar.html), defaultDockPosition = [DockPosition.Top](Overlays.DockPosition.Top.html))]
    class MyOverlay : [Overlay](Overlays.Overlay.html)
    {
        public override [VisualElement](UIElements.VisualElement.html) CreatePanelContent() => new [Label](UIElements.Label.html)("[Overlay](Overlays.Overlay.html) Contents");
    }
    

### Properties

[LeftToolbar](Overlays.DockZone.LeftToolbar.html)| Overlays are displayed in
the left toolbar.  
---|---  
[RightToolbar](Overlays.DockZone.RightToolbar.html)| Overlays are displayed in
the right toolbar.  
[TopToolbar](Overlays.DockZone.TopToolbar.html)| Overlays are displayed in the
top toolbar.  
[BottomToolbar](Overlays.DockZone.BottomToolbar.html)| Overlays are displayed
in the bottom toolbar.  
[LeftColumn](Overlays.DockZone.LeftColumn.html)| Overlays are displayed in the
left column.  
[RightColumn](Overlays.DockZone.RightColumn.html)| Overlays are displayed in
the right column.  
[Floating](Overlays.DockZone.Floating.html)| Overlays are not bound to a
toolbar or column.  
  
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

