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

#  [SerializedProperty](SerializedProperty.html).DataEquals

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

public static bool DataEquals([SerializedProperty](SerializedProperty.html) x,
[SerializedProperty](SerializedProperty.html) y);

### Description

Compares the data for two SerializedProperties. This method ignores paths and
SerializedObjects.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class SerializedPropertyDataEqualsExample : [ScriptableObject](ScriptableObject.html)
    {
        [Serializable]
        public struct SomeData
        {
            public string aStringValue;
            public float aFloatValue;
        }  
      
        [Serializable]
        public struct SomeOtherData
        {
            public string anotherStringValue;
            public float anotherFloatValue;
        }  
      
        [[SerializeField](SerializeField.html)]
        SomeData someData;
        [[SerializeField](SerializeField.html)]
        SomeOtherData[] otherDataArray;  
      
        static bool AreBothPropertiesEquals()
        {
            // Create an instance of the [ScriptableObject](ScriptableObject.html)
            var testObject = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<SerializedPropertyDataEqualsExample>();
            // Set the first class to some values
            testObject.someData.aStringValue = "ThisValue";
            testObject.someData.aFloatValue = 5.1f;
            // Set the first array entry of the second class to the exact same values
            testObject.otherDataArray = new SomeOtherData[1];
            testObject.otherDataArray[0].anotherStringValue = "ThisValue";
            testObject.otherDataArray[0].anotherFloatValue = 5.1f;  
      
            var serializedObject = new [SerializedObject](SerializedObject.html)(testObject);
            // Serialized property that refers to data from the first class
            var propertyOne = serializedObject.FindProperty("someData");
            // [SerializedProperty](SerializedProperty.html) that refers to data from the first entry of the second class array
            var propertyTwo = serializedObject.FindProperty("otherDataArray.Array.data[0]");
            // Compare data from each [SerializedProperty](SerializedProperty.html).
            bool result = [SerializedProperty.DataEquals](SerializedProperty.DataEquals.html)(propertyOne, propertyTwo);  
      
            serializedObject.Dispose();
            DestroyImmediate(testObject);
            return result;
        }  
      
        [[MenuItem](MenuItem.html)("Example/SerializedPropertyDataEqualsExample")]
        static void TestMethod()
        {
            [Debug.Log](Debug.Log.html)("Are properties equals ? " + AreBothPropertiesEquals());
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

