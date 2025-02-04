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

#  [EditorGUILayout](EditorGUILayout.html).Vector3Field

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

public static [Vector3](Vector3.html) Vector3Field(string label,
[Vector3](Vector3.html) value, params GUILayoutOption[] options);

## Declaration

public static [Vector3](Vector3.html)
Vector3Field([GUIContent](GUIContent.html) label, [Vector3](Vector3.html)
value, params GUILayoutOption[] options);

### Parameters

label | Label to display above the field.  
---|---  
value | The value to edit.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](GUILayout.Width.html),
[GUILayout.Height](GUILayout.Height.html),
[GUILayout.MinWidth](GUILayout.MinWidth.html),
[GUILayout.MaxWidth](GUILayout.MaxWidth.html),
[GUILayout.MinHeight](GUILayout.MinHeight.html),
[GUILayout.MaxHeight](GUILayout.MaxHeight.html),
[GUILayout.ExpandWidth](GUILayout.ExpandWidth.html),
[GUILayout.ExpandHeight](GUILayout.ExpandHeight.html).  
  
### Returns

**Vector3** The value entered by the user.

### Description

Make an X, Y & Z field for entering a [Vector3](Vector3.html).

![](../StaticFiles/ScriptRefImages/EditorGUILayoutVector3Field.png)  
_Measure the distance between 2 GameObjects or 2 positions in 3D space._

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class EditorGUILayoutVector3Field : UnityEditor.EditorWindow
    {
        float distance = 0f;
        [Vector3](Vector3.html) obj1;
        [Vector3](Vector3.html) obj2;  
      
        [[MenuItem](MenuItem.html)("Examples/Measure Distance between 2 objects")]
        static void Init()
        {
            EditorGUILayoutVector3Field window = (EditorGUILayoutVector3Field)[EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(EditorGUILayoutVector3Field), true, "My Empty Window");
            window.Show();
        }  
      
        void OnGUI()
        {
            [GUILayout.Label](GUILayout.Label.html)("Select an object in the [Hierarchy](Unity.Hierarchy.Hierarchy.html) view and click 'Capture [Position](UIElements.Position.html)'");
            [EditorGUILayout.BeginHorizontal](EditorGUILayout.BeginHorizontal.html)();
            obj1 = [EditorGUILayout.Vector3Field](EditorGUILayout.Vector3Field.html)("[GameObject](GameObject.html) 1:", obj1);
            if ([GUILayout.Button](GUILayout.Button.html)("Capture [Position](UIElements.Position.html)"))
                obj1 = Selection.activeTransform.position;
            [EditorGUILayout.EndHorizontal](EditorGUILayout.EndHorizontal.html)();  
      
            [EditorGUILayout.BeginHorizontal](EditorGUILayout.BeginHorizontal.html)();
            obj2 = [EditorGUILayout.Vector3Field](EditorGUILayout.Vector3Field.html)("[GameObject](GameObject.html) 2:", obj2);
            if ([GUILayout.Button](GUILayout.Button.html)("Capture [Position](UIElements.Position.html)"))
                obj2 = Selection.activeTransform.position;
            [EditorGUILayout.EndHorizontal](EditorGUILayout.EndHorizontal.html)();
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("Distance:", distance.ToString());
            if ([GUILayout.Button](GUILayout.Button.html)("Close"))
                this.Close();
        }  
      
        void OnInspectorUpdate()
        {
            distance = [Vector3.Distance](Vector3.Distance.html)(obj1, obj2);
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

