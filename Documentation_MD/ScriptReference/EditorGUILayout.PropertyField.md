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

#  [EditorGUILayout](EditorGUILayout.html).PropertyField

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

public static bool PropertyField([SerializedProperty](SerializedProperty.html)
property, params GUILayoutOption[] options);

## Declaration

public static bool PropertyField([SerializedProperty](SerializedProperty.html)
property, [GUIContent](GUIContent.html) label, params GUILayoutOption[]
options);

## Declaration

public static bool PropertyField([SerializedProperty](SerializedProperty.html)
property, bool includeChildren, params GUILayoutOption[] options);

## Declaration

public static bool PropertyField([SerializedProperty](SerializedProperty.html)
property, [GUIContent](GUIContent.html) label, bool includeChildren, params
GUILayoutOption[] options);

### Parameters

property | The SerializedProperty to make a field for.  
---|---  
label | Optional label to use. If not specified the label of the property itself is used. Use GUIContent.none to not display a label at all.  
includeChildren | If `true` the property including children is drawn; otherwise only the control itself (such as only a foldout but nothing below it).  
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

**bool** True if the property has children, is expanded, and `includeChildren`
is set to false; otherwise false. You can use it to determine the `isExpanded`
state of the property and customize the rendering of children if necessary.

### Description

Make a field for [SerializedProperty](SerializedProperty.html).

Use this when you want to customise the look of the options for a GameObject
in the Inspector. Use this to create fields for Serialized Properties. More
information on changing the Editor is available in the [Editor](Editor.html)
section.  
  
Additional resources: [SerializedProperty](SerializedProperty.html),
[SerializedObject](SerializedObject.html).

    
    
    //The scripts below show how to use a propertyField to change your editor.
    //Attach this first script to the [GameObject](GameObject.html) that you would like to control. Add code in this script for any of the actions you require.  
      
    using UnityEngine;  
      
    public class MyGameObjectScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public int m_MyInt = 75;
        public [Vector3](Vector3.html) m_MyVector = new [Vector3](Vector3.html)(20, 1, 0);
        public [GameObject](GameObject.html) m_MyGameObject;
    }
    
    
    
    //This next script shows how to call upon variables from the "MyGameObject" Script (the first script) to make custom fields in the Inspector for these variables.  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // Custom [Editor](Editor.html) using SerializedProperties.
    // [Automatic](Android.AndroidGame.Automatic.html) handling of multi-object editing, undo, and Prefab overrides.
    [[CustomEditor](CustomEditor.html)(typeof(MyGameObjectScript))]
    [[CanEditMultipleObjects](CanEditMultipleObjects.html)]
    public class EditorGUILayoutPropertyField : [Editor](Editor.html)
    {
        [SerializedProperty](SerializedProperty.html) m_IntProp;
        [SerializedProperty](SerializedProperty.html) m_VectorProp;
        [SerializedProperty](SerializedProperty.html) m_GameObjectProp;  
      
        void OnEnable()
        {
            // Fetch the objects from the [GameObject](GameObject.html) script to display in the inspector
            m_IntProp = serializedObject.FindProperty("m_MyInt");
            m_VectorProp = serializedObject.FindProperty("m_MyVector");
            m_GameObjectProp = serializedObject.FindProperty("m_MyGameObject");
        }  
      
        public override void OnInspectorGUI()
        {
            //The variables and [GameObject](GameObject.html) from the MyGameObject script are displayed in the Inspector with appropriate labels
            [EditorGUILayout.PropertyField](EditorGUILayout.PropertyField.html)(m_IntProp, new [GUIContent](GUIContent.html)("Int Field"), [GUILayout.Height](GUILayout.Height.html)(20));
            [EditorGUILayout.PropertyField](EditorGUILayout.PropertyField.html)(m_VectorProp, new [GUIContent](GUIContent.html)("Vector Object"));
            [EditorGUILayout.PropertyField](EditorGUILayout.PropertyField.html)(m_GameObjectProp, new [GUIContent](GUIContent.html)("Game Object"));  
      
            // Apply changes to the serializedProperty - always do this at the end of OnInspectorGUI.
            serializedObject.ApplyModifiedProperties();
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

