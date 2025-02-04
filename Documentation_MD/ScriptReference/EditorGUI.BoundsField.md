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

#  [EditorGUI](EditorGUI.html).BoundsField

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

public static [Bounds](Bounds.html) BoundsField([Rect](Rect.html) position,
[Bounds](Bounds.html) value);

## Declaration

public static [Bounds](Bounds.html) BoundsField([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, [Bounds](Bounds.html) value);

### Parameters

position | Rectangle on the screen to use for the field.  
---|---  
label | Optional label to display above the field.  
value | The value to edit.  
  
### Returns

**Bounds** The value entered by the user.

### Description

Makes Center and Extents field for entering a [Bounds](Bounds.html).

![](../StaticFiles/ScriptRefImages/EditorGUIBoundsField.png)  
_Bounds field in an Editor Window._  
  
See also [Extending the editor](../Manual/ExtendingTheEditor.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    
    // Simple script that shows radius of bounds of selected [MeshFilter](MeshFilter.html)  
      
    class EditorGUILayoutBoundsField : [EditorWindow](EditorWindow.html)
    {
        float radius = 0;
        [Bounds](Bounds.html) bounds;  
      
        [[MenuItem](MenuItem.html)("Examples/Show Radius of mesh bounds")]
        static void Init()
        {
            var window = GetWindow<EditorGUILayoutBoundsField>();
            window.Show();
        }  
      
        void OnGUI()
        {
            [GUILayout.Label](GUILayout.Label.html)("Select a mesh in the [Hierarchy](Unity.Hierarchy.Hierarchy.html) view and click 'Capture [Bounds](Bounds.html)'");
            [EditorGUILayout.BeginHorizontal](EditorGUILayout.BeginHorizontal.html)();
            bounds = [EditorGUILayout.BoundsField](EditorGUILayout.BoundsField.html)("[Mesh](Mesh.html) bounds:", bounds);  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Capture [Bounds](Bounds.html)") && [Selection.activeTransform](Selection-activeTransform.html))
            {
                [MeshFilter](MeshFilter.html) meshFilter = Selection.activeTransform.GetComponentInChildren<[MeshFilter](MeshFilter.html)>();
                if (meshFilter)
                {
                    bounds = meshFilter.sharedMesh.bounds;
                }
            }
            [EditorGUILayout.EndHorizontal](EditorGUILayout.EndHorizontal.html)();  
      
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("Radius:", bounds.size.magnitude.ToString());
            if ([GUILayout.Button](GUILayout.Button.html)("Close"))
            {
                this.Close();
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

