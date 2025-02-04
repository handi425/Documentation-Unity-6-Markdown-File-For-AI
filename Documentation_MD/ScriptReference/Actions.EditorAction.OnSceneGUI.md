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

#  [EditorAction](Actions.EditorAction.html).OnSceneGUI

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

public void OnSceneGUI([SceneView](SceneView.html) sceneView);

### Parameters

sceneView | The Scene view that `Actions.EditorAction.OnSceneGUI` is called in.  
---|---  
  
### Description

Callback raised when the Scene view calls OnGUI.

Use this method to implement any handles or interactive code. This is
equivalent in functionality to
[EditorTool.OnToolGUI](EditorTools.EditorTool.OnToolGUI.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Actions;
    using UnityEditor.Overlays;
    using UnityEngine;
    using UnityEngine.UIElements;
    
    public class EditorActionSampleOverlay : [Overlay](Overlays.Overlay.html)
    {
        [Vector3Field](UIElements.Vector3Field.html) m_Field;
    
        public [Action](Unity.Android.Gradle.Manifest.Action.html)<[Vector3](Vector3.html)> positionChanged;
    
        public void SetPosition([Vector3](Vector3.html) position)
        {
            m_Field?.SetValueWithoutNotify(position);
        }
    
        public override [VisualElement](UIElements.VisualElement.html) CreatePanelContent()
        {
            m_Field = new [Vector3Field](UIElements.Vector3Field.html)();
            m_Field.RegisterValueChangedCallback((evt) => positionChanged?.Invoke(evt.newValue));
            return m_Field;
        }
    }
    
    public class EditorActionSample : [EditorAction](Actions.EditorAction.html)
    {
        [[MenuItem](MenuItem.html)("Test/Start [Action](Unity.Android.Gradle.Manifest.Action.html) [Sample](PackageManager.UI.Sample.html)")]
        static void StartEditorActionSample()
        {
            Start(new EditorActionSample());
        }
    
        public [Vector3](Vector3.html) handlePosition = [Vector3.zero](Vector3-zero.html);
    
        EditorActionSampleOverlay m_Overlay;
    
        public EditorActionSample()
        {
            // Create the overlay when the action is created
            m_Overlay = new EditorActionSampleOverlay();
            m_Overlay.SetPosition(handlePosition);
            m_Overlay.positionChanged += (value) => handlePosition = value;
            [SceneView.AddOverlayToActiveView](SceneView.AddOverlayToActiveView.html)(m_Overlay);
            m_Overlay.displayed = true;
        }
    
        protected override void OnFinish([EditorActionResult](Actions.EditorActionResult.html) result)
        {
            // Remove the overlay when the action is finished
            [SceneView.RemoveOverlayFromActiveView](SceneView.RemoveOverlayFromActiveView.html)(m_Overlay);
    
            [Debug.Log](Debug.Log.html)($"[Action](Unity.Android.Gradle.Manifest.Action.html) Finished [{result}] with position: {handlePosition}");
        }
    
        public override void OnSceneGUI([SceneView](SceneView.html) sceneView)
        {
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
            handlePosition = [Handles.PositionHandle](Handles.PositionHandle.html)(handlePosition, [Quaternion.identity](Quaternion-identity.html));
    
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                m_Overlay.SetPosition(handlePosition);
            }
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

