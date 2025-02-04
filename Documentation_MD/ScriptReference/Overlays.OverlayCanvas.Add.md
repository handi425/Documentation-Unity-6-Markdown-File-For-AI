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

#  [OverlayCanvas](Overlays.OverlayCanvas.html).Add(Overlay,bool)

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

### Parameters

overlay | The Overlay to add.  
---|---  
show | True to display the Overlay immediately, false to add without displaying.  
  
### Description

Add an [Overlay](Overlays.Overlay.html) to this canvas. Added Overlays will be
displayed in the associated [EditorWindow](EditorWindow.html) until they are
removed.

In most cases, Overlays are instantiated automatically using
[OverlayAttribute](Overlays.OverlayAttribute.html). However, it is also
possible to add and remove Overlays from an
[OverlayCanvas](Overlays.OverlayCanvas.html) directly. This is useful for
short-lived Overlays that require some context. E.g., as an extension of an
Editor.  
  
Overlays added using this method must implement
[ITransientOverlay](Overlays.ITransientOverlay.html). An
[Overlay](Overlays.Overlay.html) may only belong to a single
[OverlayCanvas](Overlays.OverlayCanvas.html). To display an
[Overlay](Overlays.Overlay.html) in multiple windows, you must instantiate an
[Overlay](Overlays.Overlay.html) for each window.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEditor.Overlays;
    using UnityEngine.UIElements;  
      
    // Attach this [MonoBehaviour](MonoBehaviour.html) to a [GameObject](GameObject.html) to view the example [Overlay](Overlays.Overlay.html) in the last active [Scene](SceneManagement.Scene.html) View
    class OverlayCanvasExample : [MonoBehaviour](MonoBehaviour.html) {}  
      
    // An [Editor](Editor.html) for our OverlayCanvasExample [MonoBehaviour](MonoBehaviour.html). This will show and hide the example [Overlay](Overlays.Overlay.html) when a [GameObject](GameObject.html)
    // with the OverlayCanvasExample component is selected and deselected.
    [[CustomEditor](CustomEditor.html)(typeof(OverlayCanvasExample))]
    class OverlayCanvasExampleEditor : UnityEditor.Editor
    {
        ExampleEditorOverlay m_Overlay;  
      
        void OnEnable()
        {
            // Create a new [Overlay](Overlays.Overlay.html) with a label indicating the selected [GameObject](GameObject.html) name.
            m_Overlay = new ExampleEditorOverlay(name);
            SceneView.lastActiveSceneView.overlayCanvas.Add(m_Overlay);
        }  
      
        void OnDisable()
        {
            // If the [Overlay](Overlays.Overlay.html) has not already been closed, close it when this editor is disabled. Added Overlays will
            // persist until they are closed.
            m_Overlay?.Close();
        }
    }  
      
    class ExampleEditorOverlay : [Overlay](Overlays.Overlay.html), [ITransientOverlay](Overlays.ITransientOverlay.html)
    {
        // Overlays added directly to the canvas must implement [ITransientOverlay](Overlays.ITransientOverlay.html), meaning they control their own lifecycle.
        public bool visible => true;  
      
        string m_Message;  
      
        public ExampleEditorOverlay(string message)
        {
            m_Message = message;
        }  
      
        public override [VisualElement](UIElements.VisualElement.html) CreatePanelContent()
        {
            var root = new [VisualElement](UIElements.VisualElement.html)();
            root.Add(new [Label](UIElements.Label.html)(m_Message));
            root.Add(new [Button](UIElements.Button.html)(Close) { text = "Close" });
            return root;
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

