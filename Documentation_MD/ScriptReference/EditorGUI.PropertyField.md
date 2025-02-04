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

#  [EditorGUI](EditorGUI.html).PropertyField

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

public static bool PropertyField([Rect](Rect.html) position,
[SerializedProperty](SerializedProperty.html) property, bool includeChildren =
false);

## Declaration

public static bool PropertyField([Rect](Rect.html) position,
[SerializedProperty](SerializedProperty.html) property,
[GUIContent](GUIContent.html) label, bool includeChildren = false);

### Parameters

position | Rectangle on the screen to use for the property field.  
---|---  
property | The SerializedProperty to make a field for.  
label | Optional label to use. If not specified the label of the property itself is used. Use GUIContent.none to not display a label at all.  
includeChildren | If `true` the property including children is drawn; otherwise only the control itself (such as only a foldout but nothing below it).  
  
### Returns

**bool** True if the property has children and is expanded and includeChildren
was set to false; otherwise false.

### Description

Use this to make a field for a [SerializedProperty](SerializedProperty.html)
in the Editor.

Additional resources: [SerializedProperty](SerializedProperty.html),
[SerializedObject](SerializedObject.html).

    
    
    //Attach a script like this to the [GameObject](GameObject.html) you would like to have a custom [Editor](Editor.html) window.  
      
    using UnityEngine;  
      
    public class MyScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public int myInt = 90;
    }
    
    
    
    //Create a folder and name it “[Editor](Editor.html)” and place this second script within it. To do this right click within the Assets directory and go to Create>[Folder](WSA.Folder.html)
    //Ensure you insert your first script’s name as a parameter in the [CustomEditor](CustomEditor.html) e.g. [[CustomEditor](CustomEditor.html)(typeof(MyScript))]  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // Custom [Editor](Editor.html) using SerializedProperties.
    // Make sure to put the name of the script on your [GameObject](GameObject.html) in here
    [[CustomEditor](CustomEditor.html)(typeof(MyScript))]
    // [Automatic](Android.AndroidGame.Automatic.html) handling of multi-object editing, undo, and Prefab overrides.
    [[CanEditMultipleObjects](CanEditMultipleObjects.html)]  
      
    public class EditorGUIPropertyField : [Editor](Editor.html)
    {
        [SerializedProperty](SerializedProperty.html) m_IntProperty;  
      
        void OnEnable()
        {
            // Fetch the objects from the MyScript script to display in the inspector
            m_IntProperty = serializedObject.FindProperty("myInt");
        }  
      
        public override void OnInspectorGUI()
        {
            //The variables and [GameObject](GameObject.html) from the [GameObject](GameObject.html) script are displayed in the Inspector and have the appropriate label
            [EditorGUI.PropertyField](EditorGUI.PropertyField.html)(new [Rect](Rect.html)(0, 300, 500, 30), m_IntProperty, new [GUIContent](GUIContent.html)("Int : "));  
      
            // Apply changes to the serializedProperty - always do this in the end of OnInspectorGUI.
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

