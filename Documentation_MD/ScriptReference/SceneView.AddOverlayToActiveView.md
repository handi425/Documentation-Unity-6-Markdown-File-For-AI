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

#  [SceneView](SceneView.html).AddOverlayToActiveView

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

public static void AddOverlayToActiveView(T overlay);

### Parameters

overlay | The [Overlay](Overlays.Overlay.html) to add.  
---|---  
  
### Description

Add an [Overlay](Overlays.Overlay.html) to be displayed in the last focused
Scene View. Overlays added to this static list will be automatically moved to
the last active Scene View, and are displayed until removed.

See also
[SceneView.RemoveOverlayFromActiveView](SceneView.RemoveOverlayFromActiveView.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.EditorTools;
    using UnityEditor.Overlays;
    using UnityEditor.UIElements;
    using UnityEngine;
    using UnityEngine.UIElements;  
      
    // An [EditorTool](EditorTools.EditorTool.html) that shows an [Overlay](Overlays.Overlay.html) in the active scene view while enabled.
    [[EditorTool](EditorTools.EditorTool.html)("[Overlay](Overlays.Overlay.html) [Tool](Tool.html) Example", typeof([Transform](Transform.html)))]
    class ToolWithOverlay : [EditorTool](EditorTools.EditorTool.html)
    {
        ActiveSceneViewOverlay m_Overlay;  
      
        void OnEnable()
        {
            m_Overlay = new ActiveSceneViewOverlay(targets.Cast<[Transform](Transform.html)>().ToArray());
            [SceneView.AddOverlayToActiveView](SceneView.AddOverlayToActiveView.html)(m_Overlay);
        }  
      
        void OnDisable()
        {
            [SceneView.RemoveOverlayFromActiveView](SceneView.RemoveOverlayFromActiveView.html)(m_Overlay);
        }
    }  
      
    // A simple [Overlay](Overlays.Overlay.html) that moves a collection of transforms by some translation.
    class ActiveSceneViewOverlay : [Overlay](Overlays.Overlay.html)
    {
        [Vector3Field](UIElements.Vector3Field.html) m_Translation;
        [Transform](Transform.html)[] m_Selection;  
      
        public ActiveSceneViewOverlay([Transform](Transform.html)[] selection)
        {
            m_Selection = selection;
        }  
      
        public override [VisualElement](UIElements.VisualElement.html) CreatePanelContent()
        {
            var root = new [VisualElement](UIElements.VisualElement.html)();
            root.Add(m_Translation = new [Vector3Field](UIElements.Vector3Field.html)("Translation"));
            root.Add(new [Button](UIElements.Button.html)(MoveSelectionUp) { text = "Move [Selection](Selection.html) Up" });
            m_Translation.SetValueWithoutNotify([Vector3.up](Vector3-up.html));
            m_Translation.style.minWidth = 300;
            return root;
        }  
      
        void MoveSelectionUp()
        {
            [Undo.RecordObjects](Undo.RecordObjects.html)(m_Selection.ToArray(), "Move [Selection](Selection.html)");
            foreach (var transform in m_Selection)
                transform.position += m_Translation.value;
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

