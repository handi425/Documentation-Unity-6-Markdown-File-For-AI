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

# GizmoUtility

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

A static class for interacting with the Scene View icons and gizmos for types.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    
    // An [Editor](Editor.html) Window that lets you edit the gizmo and icon properties for each selected component.
    public class GizmoUtilityExample  : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Window/Gizmo Window")]
        static void Init() => GetWindow<GizmoUtilityExample>();
    
        [Vector2](Vector2.html) m_Scroll;
    
        void OnEnable()
        {
            autoRepaintOnSceneChange = true;
        }
    
        void OnGUI()
        {
            [GizmoUtility.use3dIcons](GizmoUtility-use3dIcons.html) = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("3D Icons", [GizmoUtility.use3dIcons](GizmoUtility-use3dIcons.html));
    
            EditorGUI.BeginDisabled(![GizmoUtility.use3dIcons](GizmoUtility-use3dIcons.html));
            [GizmoUtility.iconSize](GizmoUtility-iconSize.html) = [EditorGUILayout.Slider](EditorGUILayout.Slider.html)("3D Icon Size", [GizmoUtility.iconSize](GizmoUtility-iconSize.html), 0f, 1f);
            EditorGUI.EndDisabled();
    
            m_Scroll = [EditorGUILayout.BeginScrollView](EditorGUILayout.BeginScrollView.html)(m_Scroll);
    
            foreach (var go in [Selection.gameObjects](Selection-gameObjects.html))
            {
                [GUILayout.Label](GUILayout.Label.html)($"{go.name} [Gizmos](Gizmos.html)", [EditorStyles.boldLabel](EditorStyles-boldLabel.html));
    
                [EditorGUI.indentLevel](EditorGUI-indentLevel.html)++;
                foreach (var component in go.GetComponents<[Component](Component.html)>())
                {
                    // A component can have gizmos, an icon, both, or neither. A gizmo can also be disabled (the [Editor](Editor.html)
                    // is collapsed in the Inspector).
                    if ([GizmoUtility.TryGetGizmoInfo](GizmoUtility.TryGetGizmoInfo.html)(component.GetType(), out [GizmoInfo](GizmoInfo.html) info))
                    {
                        [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
    
                        if (info.hasGizmo)
                            info.gizmoEnabled = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)($"{info.name} Gizmo", info.gizmoEnabled);
    
                        if (info.hasIcon)
                            info.iconEnabled = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)($"{info.name} Icon", info.iconEnabled);
    
                        if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
                            [GizmoUtility.ApplyGizmoInfo](GizmoUtility.ApplyGizmoInfo.html)(info);
                    }
                }
                [EditorGUI.indentLevel](EditorGUI-indentLevel.html)--;
            }
    
            [EditorGUILayout.EndScrollView](EditorGUILayout.EndScrollView.html)();
        }
    }
    

### Static Properties

[iconSize](GizmoUtility-iconSize.html)| Control the size that 3D icons render
in the Scene View.  
---|---  
[use3dIcons](GizmoUtility-use3dIcons.html)| Determines whether icons in the
Scene View are a fixed size (false) or scaled relative to distance from the
camera and iconSize.  
  
### Static Methods

[ApplyGizmoInfo](GizmoUtility.ApplyGizmoInfo.html)| Apply gizmoEnabled and
iconEnabled for a GizmoInfo object.  
---|---  
[GetGizmoInfo](GizmoUtility.GetGizmoInfo.html)| Get GizmoInfo for all
components with gizmos or icons in the project.  
[SetGizmoEnabled](GizmoUtility.SetGizmoEnabled.html)| Enable or disable gizmo
rendering in the Scene View for a component type. Gizmos are the simple lines
and guides drawn by component editors. For example, the Camera frustum
guidelines are gizmos.  
[SetIconEnabled](GizmoUtility.SetIconEnabled.html)| Enable or disable icon
rendering for all objects in the Scene View for a component type.  
[TryGetGizmoInfo](GizmoUtility.TryGetGizmoInfo.html)| Get a GizmoInfo for a
type if it exists.  
  
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

