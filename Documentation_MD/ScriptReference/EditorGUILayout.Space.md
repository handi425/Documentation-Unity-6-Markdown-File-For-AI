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

#  [EditorGUILayout](EditorGUILayout.html).Space

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

public static void Space();

## Declaration

public static void Space(float width);

## Declaration

public static void Space(float width, bool expand);

### Parameters

width | The width of the empty space. Use this for horizontal layout.  
---|---  
expand | Option passed to enable or disable horizontal expansion.  
  
### Description

Make a small space between the previous control and the following.

![](../StaticFiles/ScriptRefImages/InspectorTitlebarUsageSpace.png)  
_Custom inspector that shows the X,Y,Z,W quaternion components of a
transform._

    
    
    // Create a custom transform inspector that shows the X,Y,Z,W quaternion components
    // instead of the rotation angles.  
      
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class EditorGUILayoutSpaceField : [EditorWindow](EditorWindow.html)
    {
        bool fold = true;
        [Vector4](Vector4.html) rotationComponents;
        [Transform](Transform.html) selectedTransform;  
      
        [[MenuItem](MenuItem.html)("Examples/[Space](Space.html) between controls")]
        static void Init()
        {
            [EditorWindow](EditorWindow.html) window = GetWindow(typeof(EditorGUILayoutSpaceField));
            window.Show();
        }  
      
        void OnGUI()
        {
            if ([Selection.activeGameObject](Selection-activeGameObject.html))
            {
                selectedTransform = Selection.activeGameObject.transform;
                fold = [EditorGUILayout.InspectorTitlebar](EditorGUILayout.InspectorTitlebar.html)(fold, selectedTransform);
                if (fold)
                {
                    selectedTransform.position =
                        [EditorGUILayout.Vector3Field](EditorGUILayout.Vector3Field.html)("[Position](UIElements.Position.html)", selectedTransform.position);
                    [EditorGUILayout.Space](EditorGUILayout.Space.html)();  
      
                    rotationComponents =
                        [EditorGUILayout.Vector4Field](EditorGUILayout.Vector4Field.html)("Detailed Rotation",
                            QuaternionToVector4(selectedTransform.localRotation));  
      
                    [EditorGUILayout.Space](EditorGUILayout.Space.html)();
                    selectedTransform.localScale =
                        [EditorGUILayout.Vector3Field](EditorGUILayout.Vector3Field.html)("[Scale](UIElements.Scale.html)", selectedTransform.localScale);
                }
                selectedTransform.localRotation = ConvertToQuaternion(rotationComponents);
                [EditorGUILayout.Space](EditorGUILayout.Space.html)();
            }
        }  
      
        [Quaternion](Quaternion.html) ConvertToQuaternion([Vector4](Vector4.html) v4)
        {
            return new [Quaternion](Quaternion.html)(v4.x, v4.y, v4.z, v4.w);
        }  
      
        [Vector4](Vector4.html) QuaternionToVector4([Quaternion](Quaternion.html) q)
        {
            return new [Vector4](Vector4.html)(q.x, q.y, q.z, q.w);
        }  
      
        void OnInspectorUpdate()
        {
            this.Repaint();
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

