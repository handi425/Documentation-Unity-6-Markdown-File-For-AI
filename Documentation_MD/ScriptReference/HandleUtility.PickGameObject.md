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

#  [HandleUtility](HandleUtility.html).PickGameObject

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

public static [GameObject](GameObject.html)
PickGameObject([Vector2](Vector2.html) position, out int materialIndex);

## Declaration

public static [GameObject](GameObject.html)
PickGameObject([Vector2](Vector2.html) position, GameObject[] ignore, out int
materialIndex);

## Declaration

public static [GameObject](GameObject.html)
PickGameObject([Vector2](Vector2.html) position, GameObject[] ignore,
GameObject[] selection, out int materialIndex);

## Declaration

public static [GameObject](GameObject.html)
PickGameObject([Vector2](Vector2.html) position, bool selectPrefabRoot);

## Declaration

public static [GameObject](GameObject.html)
PickGameObject([Vector2](Vector2.html) position, bool selectPrefabRoot,
GameObject[] ignore);

## Declaration

public static [GameObject](GameObject.html)
PickGameObject([Vector2](Vector2.html) position, bool selectPrefabRoot,
GameObject[] ignore, GameObject[] filter);

## Declaration

public static [GameObject](GameObject.html)
PickGameObject([Vector2](Vector2.html) position, bool selectPrefabRoot,
GameObject[] ignore, GameObject[] filter, out int materialIndex);

### Parameters

selectPrefabRoot | Select Prefab.  
---|---  
materialIndex | Returns index into material array of the Renderer component that is closest to specified position.  
position | A position in screen coordinates. The top-left of the window is (0,0), and the bottom-right is (Screen.width, Screen.height).  
ignore | An array of GameObjects that will not be considered when selecting the nearest GameObject.  
filter | An array of GameObjects to be exclusively considered for selection. If null, all GameObjects in open scenes are eligible for selection.  
selection | An array of GameObjects to be exclusively considered for selection. If null, all GameObjects in open scenes are eligible for selection.  
  
### Returns

**GameObject** The GameObject that is under the requested position.

### Description

Pick game object closest to specified position.

HandleUtility.PickGameObject must not be called during a repaint. In most
cases it is appropriate to call during
[EventType.MouseDown](EventType.MouseDown.html) or
[EventType.MouseUp](EventType.MouseUp.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    static class ShowHovered
    {
        static [GameObject](GameObject.html) m_LastHoveredObject, m_LastClickedObject;  
      
        [InitializeOnLoadMethod]
        static void Init()
        {
            [SceneView.duringSceneGui](SceneView-duringSceneGui.html) += OnSceneGUI;
        }  
      
        static void OnSceneGUI([SceneView](SceneView.html) view)
        {
            var evt = [Event.current](Event-current.html);  
      
            // Register a control so that if no other handle is engaged, we can use the event.
            var pickingControlId = [GUIUtility.GetControlID](GUIUtility.GetControlID.html)([FocusType.Passive](FocusType.Passive.html));
            [HandleUtility.AddDefaultControl](HandleUtility.AddDefaultControl.html)(pickingControlId);  
      
            switch (evt.type)
            {
                case [EventType.MouseMove](EventType.MouseMove.html):
                {
                    var picked = [HandleUtility.PickGameObject](HandleUtility.PickGameObject.html)(evt.mousePosition, false);  
      
                    if (picked != m_LastHoveredObject)
                    {
                        m_LastHoveredObject = picked;
                        [SceneView.RepaintAll](SceneView.RepaintAll.html)();
                    }  
      
                    break;
                }  
      
                case [EventType.MouseDown](EventType.MouseDown.html):
                {
                    // Make sure to check [Tools.viewToolActive](Tools-viewToolActive.html) before consuming a mouse event, otherwise [Scene](SceneManagement.Scene.html) navigation
                    // controls will not work.
                    if (![Tools.viewToolActive](Tools-viewToolActive.html) && [HandleUtility.nearestControl](HandleUtility-nearestControl.html) == pickingControlId)
                    {
                        [GUIUtility.hotControl](GUIUtility-hotControl.html) = pickingControlId;
                        evt.Use();
                    }  
      
                    break;
                }  
      
                case [EventType.MouseUp](EventType.MouseUp.html):
                {
                    // If the hotControl is not pickingControlId, that means another control has the rights to this event.
                    if ([GUIUtility.hotControl](GUIUtility-hotControl.html) != pickingControlId)
                        return;  
      
                    var picked = [HandleUtility.PickGameObject](HandleUtility.PickGameObject.html)(evt.mousePosition, false);  
      
                    if (picked != m_LastClickedObject)
                    {
                        m_LastClickedObject = picked;
                        [SceneView.RepaintAll](SceneView.RepaintAll.html)();
                    }  
      
                    // Make sure to Use() and reset the hotControl the event if we are the active control ID.
                    evt.Use();
                    [GUIUtility.hotControl](GUIUtility-hotControl.html) = 0;
                    break;
                }
            }  
      
            [Handles.BeginGUI](Handles.BeginGUI.html)();
            [GUILayout.BeginVertical](GUILayout.BeginVertical.html)([EditorStyles.helpBox](EditorStyles-helpBox.html), [GUILayout.ExpandWidth](GUILayout.ExpandWidth.html)(false));
            [GUILayout.Label](GUILayout.Label.html)($"Last Hovered Object: {m_LastHoveredObject}");
            [GUILayout.Label](GUILayout.Label.html)($"Last Clicked Object: {m_LastClickedObject}");
            [GUILayout.EndVertical](GUILayout.EndVertical.html)();
            [Handles.EndGUI](Handles.EndGUI.html)();
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

