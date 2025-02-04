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

#  [SerializedProperty](SerializedProperty.html).isArray

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

public bool isArray;

### Description

Is this property an array? (Read Only)

Additional resources: [arraySize](SerializedProperty-arraySize.html),
[GetArrayElementAtIndex](SerializedProperty.GetArrayElementAtIndex.html).

    
    
    using System.Text;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    // Example showing the structure of [SerializedProperty](SerializedProperty.html) objects that comprise an Array property exposed by [SerializedObject](SerializedObject.html).
    // Often this structure can be ignored and [SerializedProperty.arraySize](SerializedProperty-arraySize.html) and [SerializedProperty.GetArrayElementAtIndex](SerializedProperty.GetArrayElementAtIndex.html)(0)
    // are convenient to jump straight to the size and data content.
    // But, because the specific structure is exposed when using [SerializedProperty.Next](SerializedProperty.Next.html) and [SerializedProperty.propertyPath](SerializedProperty-propertyPath.html),
    // some understanding of this structure can be useful.
    public class StructureOfArrayExample : [ScriptableObject](ScriptableObject.html)
    {
        // Serialized array
        // Note: The example would behave the same way if it was List<int>
        public string[] m_Data;  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedProperty](SerializedProperty.html)/Array Structure Example")]
        static void MenuCallback()
        {
            var log = new StringBuilder();  
      
            StructureOfArrayExample obj = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<StructureOfArrayExample>();
            obj.m_Data = new string[] { "zero", "one" };  
      
            [SerializedObject](SerializedObject.html) serializedObject = new [SerializedObject](SerializedObject.html)(obj);  
      
            // Top level property represents the entire array
            [SerializedProperty](SerializedProperty.html) serializedProperty = serializedObject.FindProperty("m_Data");
            ReportPropertyDetails(serializedProperty, log);  
      
            // Next element is a structural element ".Array".
            // This does not take any space in the serialized data, and acts much the same as the top level property
            bool visitChildren = true;
            serializedProperty.Next(visitChildren);
            ReportPropertyDetails(serializedProperty, log);  
      
            // First nested child is ".Array.size", which stores the number of elements of the array
            serializedProperty.Next(visitChildren);
            ReportPropertyDetails(serializedProperty, log);  
      
            // Next comes the first array element, ".Array.data[0]".
            // In this case it is the string "zero".  Strings are also represented as Arrays in [SerializedObject](SerializedObject.html).
            serializedProperty.Next(visitChildren);
            ReportPropertyDetails(serializedProperty, log);  
      
            // Skip past the nested content of the first string to get to the next string ("one")
            visitChildren = false;
            serializedProperty.Next(visitChildren);
            ReportPropertyDetails(serializedProperty, log);  
      
            //Will log:
            //Property path: 'm_Data' type: 'Generic' isArray: True depth: 0
            //Property path: 'm_Data.Array' type: 'Generic' isArray: True depth: 0
            //Property path: 'm_Data.Array.size' type: 'ArraySize' isArray: False depth: 1
            //Property path: 'm_Data.Array.data[0]' type: 'String' isArray: True depth: 1
            //Property path: 'm_Data.Array.data[1]' type: 'String' isArray: True depth: 1
            [Debug.Log](Debug.Log.html)(log.ToString());
        }  
      
        static void ReportPropertyDetails([SerializedProperty](SerializedProperty.html) prop, StringBuilder log)
        {
            log.AppendLine($"Property path: \'{prop.propertyPath}\' type: \'{prop.propertyType}\' isArray: {prop.isArray} depth: {prop.depth}");
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

