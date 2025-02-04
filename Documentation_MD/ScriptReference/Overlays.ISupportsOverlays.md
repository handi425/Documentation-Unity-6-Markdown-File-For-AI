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

# ISupportsOverlays

interface in UnityEditor.Overlays

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

Implement this interface to enable overlays in the
[EditorWindow](EditorWindow.html).

When [ISupportsOverlays](Overlays.ISupportsOverlays.html) is implemented, an
Overlay Canvas is automatically added to the
[VisualElement](UIElements.VisualElement.html) tree for your
[EditorWindow](EditorWindow.html).
[OverlayAttribute](Overlays.OverlayAttribute.html) will now be able to specify
this window type as a valid target for registering an
[Overlay](Overlays.Overlay.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Overlays;
    using UnityEngine;
    using UnityEngine.UIElements;
    
    class EditorWindowOverlayExample : [EditorWindow](EditorWindow.html), [ISupportsOverlays](Overlays.ISupportsOverlays.html)
    {
        [[MenuItem](MenuItem.html)("Window/[Overlay](Overlays.Overlay.html) Supported Window Example")]
        static void Init() => GetWindow<EditorWindowOverlayExample>();
    
        void OnGUI()
        {
            [GUILayout.Label](GUILayout.Label.html)("Here is some text");
            [GUILayout.FlexibleSpace](GUILayout.FlexibleSpace.html)();
            [GUILayout.Label](GUILayout.Label.html)("Plus some more text, but on the bottom of the screen.");
        }
    }
    
    [[Overlay](Overlays.Overlay.html)(typeof(EditorWindowOverlayExample), "Is Mouse Hovering Me?", true)]
    class IsMouseHoveringMe : [Overlay](Overlays.Overlay.html)
    {
        [Label](UIElements.Label.html) m_MouseLabel;
    
        public override [VisualElement](UIElements.VisualElement.html) CreatePanelContent()
        {
            m_MouseLabel = new [Label](UIElements.Label.html)();
            m_MouseLabel.style.minHeight = 40;
            m_MouseLabel.RegisterCallback<[MouseEnterEvent](UIElements.MouseEnterEvent.html)>(evt => m_MouseLabel.text = "Mouse is hovering this [Overlay](Overlays.Overlay.html) content!");
            m_MouseLabel.RegisterCallback<[MouseLeaveEvent](UIElements.MouseLeaveEvent.html)>(evt => m_MouseLabel.text = "Mouse is not hovering this [Overlay](Overlays.Overlay.html) content.");
            return m_MouseLabel;
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

