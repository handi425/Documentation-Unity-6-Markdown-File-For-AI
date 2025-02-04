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

#  [SerializedPropertyType](SerializedPropertyType.html).Generic

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

Represents an array, list, struct or class.

The Generic type is used for compound types that are serialized in-line:  
\- Arrays and lists.  
\- Structs that are user defined (e.g. not a built in Unity type).  
\- Classes that are serialized 'by value' (e.g. referenced without the
[SerializeReference](SerializeReference.html) attribute).  
\- Certain built in Unity structs, when they do not have dedicated
SerializedPropertyType enum value. For example [RectOffset](RectOffset.html)
is Generic, but [Vector3](Vector3.html) is
[SerializedPropertyType.Vector3](SerializedPropertyType.Vector3.html).  
  
  
Note: The term Generic, when used as a SerializedProperty type, should not be
confused with the unrelated C# feature of Generic classes and methods.  
  
Additional resources: [SerializedProperty.isArray](SerializedProperty-
isArray.html),
[SerializedPropertyType.ManagedReference](SerializedPropertyType.ManagedReference.html),
[SerializedPropertyType.ObjectReference](SerializedPropertyType.ObjectReference.html)

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Text;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using System.Collections.Generic;  
      
    namespace GenericObjectTypeExample
    {
        [Serializable]
        public struct ExampleStruct
        {
            public int m_Field;
        };  
      
        [Serializable]
        public class ExampleClass
        {
            public int m_Field;
        };  
      
        public class GenericTypeExample : [ScriptableObject](ScriptableObject.html)
        {
            // All these fields will be serialized
            public int[] m_ArrayOfInt;
            public List<int> m_ListOfInt;
            public ExampleStruct m_ExampleStruct = new ExampleStruct() { m_Field = 1 };
            public ExampleClass m_ExampleClass = new ExampleClass() { m_Field = 2 };  
      
            [[SerializeReference](SerializeReference.html)]
            public ExampleClass m_ManagedClass = new ExampleClass() { m_Field = 3 };  
      
            [[MenuItem](MenuItem.html)("Example/[SerializedPropertyType](SerializedPropertyType.html) Generic Example")]
            static void GenericExample()
            {
                var scriptableObject = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<GenericTypeExample>();
                using (var serializedObject = new [SerializedObject](SerializedObject.html)(scriptableObject))
                {
                    var report = new StringBuilder();  
      
                    // Generic
                    ReportType(report, serializedObject, "m_ArrayOfInt");
                    ReportType(report, serializedObject, "m_ListOfInt");
                    ReportType(report, serializedObject, "m_ExampleStruct");
                    ReportType(report, serializedObject, "m_ExampleClass");  
      
                    // Not Generic
                    ReportType(report, serializedObject, "m_ManagedClass");  
      
                    [Debug.Log](Debug.Log.html)(report.ToString());  
      
                    AccessGenericValues(serializedObject);
                }
            }  
      
            static void AccessGenericValues([SerializedObject](SerializedObject.html) serializedObject)
            {
                // "generic" type struct and objects can be retrieved directly with boxedValue
                ExampleStruct structValues = (ExampleStruct)serializedObject.FindProperty("m_ExampleStruct").boxedValue;  
      
                // Alternatively individual fields can be read
                int fieldInStruct = serializedObject.FindProperty("m_ExampleStruct.m_Field").intValue;  
      
                [Debug.Log](Debug.Log.html)($"Value of field in struct: {structValues.m_Field}, Value of field direct read: {fieldInStruct}");  
      
                // Similarly boxedValue supports writing to an inline class
                [SerializedProperty](SerializedProperty.html) inlineClass = serializedObject.FindProperty("m_ExampleClass");  
      
                // Serialize new state in a single call
                inlineClass.boxedValue = new ExampleClass() { m_Field = 4 };  
      
                // Individual fields can also be accessed
                [Debug.Log](Debug.Log.html)($"Value of field in class after write: {inlineClass.FindPropertyRelative("m_Field").intValue}");  
      
                serializedObject.ApplyModifiedProperties();
            }  
      
            static void ReportType(StringBuilder report, [SerializedObject](SerializedObject.html) serializedObject, string propertyPath)
            {
                var serializedProperty = serializedObject.FindProperty(propertyPath);
                report.AppendLine($"{propertyPath} has type {serializedProperty.propertyType}");
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

