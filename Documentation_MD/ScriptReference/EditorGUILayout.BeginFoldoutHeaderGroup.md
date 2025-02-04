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

#  [EditorGUILayout](EditorGUILayout.html).BeginFoldoutHeaderGroup

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

public static bool BeginFoldoutHeaderGroup(bool foldout, string content,
[GUIStyle](GUIStyle.html) style = EditorStyles.foldoutHeader, Action<Rect>
menuAction, [GUIStyle](GUIStyle.html) menuIcon);

## Declaration

public static bool BeginFoldoutHeaderGroup(bool foldout,
[GUIContent](GUIContent.html) content, [GUIStyle](GUIStyle.html) style =
EditorStyles.foldoutHeader, Action<Rect> menuAction, [GUIStyle](GUIStyle.html)
menuIcon);

### Parameters

foldout | The shown foldout state.  
---|---  
content | The label to show.  
style | Optional [GUIStyle](GUIStyle.html).  
menuAction | The action that happens when you click the icon.  
menuIcon | Optional [GUIStyle](GUIStyle.html) for icon.  
  
### Returns

**bool** The foldout state selected by the user. If true, you should render
sub-objects.

### Description

Make a label with a foldout arrow to the left of it.

This is useful for folder-like structures, where child objects only appear if
you've unfolded the parent folder. This control cannot be nested in another
BeginFoldoutHeaderGroup. To use multiple of these foldouts, you must end each
method with EndFoldoutHeaderGroup.  
  
![](../StaticFiles/ScriptRefImages/EditorGUILayoutFoldoutHeader.png)  
_Create a foldable header menu that hides or shows the selected Transform._

    
    
    // Create a foldable header menu that hides or shows the selected [Transform](Transform.html) position.
    // If you have not selected a [Transform](Transform.html), the [Foldout](UIElements.Foldout.html) item stays folded until
    // you select a [Transform](Transform.html).  
      
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class FoldoutHeaderUsage : [EditorWindow](EditorWindow.html)
    {
        bool showPosition = true;
        string status = "Select a [GameObject](GameObject.html)";  
      
        [[MenuItem](MenuItem.html)("Examples/[Foldout](UIElements.Foldout.html) Header Usage")]
        static void CreateWindow()
        {
            GetWindow<FoldoutHeaderUsage>();
        }  
      
        public void OnGUI()
        {
            showPosition = [EditorGUILayout.BeginFoldoutHeaderGroup](EditorGUILayout.BeginFoldoutHeaderGroup.html)(showPosition, status);  
      
            if (showPosition)
                if ([Selection.activeTransform](Selection-activeTransform.html))
                {
                    Selection.activeTransform.position =
                        [EditorGUILayout.Vector3Field](EditorGUILayout.Vector3Field.html)("[Position](UIElements.Position.html)", Selection.activeTransform.position);
                    status = Selection.activeTransform.name;
                }  
      
            if (![Selection.activeTransform](Selection-activeTransform.html))
            {
                status = "Select a [GameObject](GameObject.html)";
                showPosition = false;
            }
            // End the [Foldout](UIElements.Foldout.html) Header that we began above.
            [EditorGUILayout.EndFoldoutHeaderGroup](EditorGUILayout.EndFoldoutHeaderGroup.html)();
        }
    }
    

![](../StaticFiles/ScriptRefImages/EditorGUILayoutFoldoutHeaderMenu.png)  
_Create a menu item action that moves the selected object to 0,0,0 when you
click it._

    
    
    // Create a foldable header menu that hides or shows the selected [Transform](Transform.html) position.
    // If you have not selected a [Transform](Transform.html), the [Foldout](UIElements.Foldout.html) item stays folded until
    // you select a [Transform](Transform.html).  
      
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class FoldoutHeaderUsage : [EditorWindow](EditorWindow.html)
    {
        bool showPosition = true;
        string status = "Select a [GameObject](GameObject.html)";  
      
        [[MenuItem](MenuItem.html)("Examples/[Foldout](UIElements.Foldout.html) Header Usage")]
        static void CreateWindow()
        {
            GetWindow<FoldoutHeaderUsage>();
        }  
      
        public void OnGUI()
        {
            showPosition = [EditorGUILayout.BeginFoldoutHeaderGroup](EditorGUILayout.BeginFoldoutHeaderGroup.html)(showPosition, status, null, ShowHeaderContextMenu);  
      
            if (showPosition)
                if ([Selection.activeTransform](Selection-activeTransform.html))
                {
                    Selection.activeTransform.position =
                        [EditorGUILayout.Vector3Field](EditorGUILayout.Vector3Field.html)("[Position](UIElements.Position.html)", Selection.activeTransform.position);
                    status = Selection.activeTransform.name;
                }  
      
            if (![Selection.activeTransform](Selection-activeTransform.html))
            {
                status = "Select a [GameObject](GameObject.html)";
                showPosition = false;
            }
            // End the [Foldout](UIElements.Foldout.html) Header that we began above.
            [EditorGUILayout.EndFoldoutHeaderGroup](EditorGUILayout.EndFoldoutHeaderGroup.html)();
        }  
      
        void ShowHeaderContextMenu([Rect](Rect.html) position)
        {
            var menu = new [GenericMenu](GenericMenu.html)();
            menu.AddItem(new [GUIContent](GUIContent.html)("Move to (0,0,0)"), false, OnItemClicked);
            menu.DropDown(position);
        }  
      
        void OnItemClicked()
        {
            [Undo.RecordObject](Undo.RecordObject.html)([Selection.activeTransform](Selection-activeTransform.html), "Moving to center of world");
            Selection.activeTransform.position = [Vector3.zero](Vector3-zero.html);
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

