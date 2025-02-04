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

#  [SerializedProperty](SerializedProperty.html).minArraySize

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

public int minArraySize;

### Description

The smallest number of elements in the array across all target objects. (Read
Only)

If the SerializedObject contains multiple objects, this property returns the
smallest number of elements. Unlike
[SerializedProperty.arraySize](SerializedProperty-arraySize.html) the minimum
size is returned even if it is larger than
[SerializedObject.maxArraySizeForMultiEditing](SerializedObject-
maxArraySizeForMultiEditing.html). In that case
SerializedObject.maxArraySizeForMultiEditing could be increased to permit
access to the array contents.  
  
When the SerializedObject contains only a single object, this property behaves
in the same way as [SerializedProperty.arraySize](SerializedProperty-
arraySize.html) and returns the true array size.  
  
Additional resources: [arraySize](SerializedProperty-arraySize.html),
[isArray](SerializedProperty-isArray.html),
[SerializedObject.targetObjects](SerializedObject-targetObjects.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class MinArraySizeExample : [ScriptableObject](ScriptableObject.html)
    {
        public int[] m_data;  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedProperty](SerializedProperty.html) MinArraySize Example")]
        static void TestMethod()
        {
            const int largeArraySize = 100; // Larger than the default maxArraySizeForMultiEditing value of 64  
      
            MinArraySizeExample obj1 = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<MinArraySizeExample>();
            obj1.m_data = new int[largeArraySize];  
      
            for (int i = 0; i < largeArraySize; i++)
                obj1.m_data[i] = i;  
      
            // Second object with its own copy of the large array
            MinArraySizeExample obj2 = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<MinArraySizeExample>();
            obj2.m_data = obj1.m_data;  
      
            // Create serialized object for manipulating both objects
            [SerializedObject](SerializedObject.html) serializedObject = new [SerializedObject](SerializedObject.html)(new Object[] { obj1, obj2 });
            [SerializedProperty](SerializedProperty.html) property = serializedObject.FindProperty("m_data");  
      
            // arraySize returns 0 but minArraySize returns largeArraySize
            [Debug.LogFormat](Debug.LogFormat.html)("Array Size: {0}\nMin Array Size: {1}\nMax Array Size: {2}",
                property.arraySize, property.minArraySize, serializedObject.maxArraySizeForMultiEditing);  
      
            // Any call to GetArrayElementAtIndex() at this point would fail  
      
            // Extend the max permitted array size
            serializedObject.maxArraySizeForMultiEditing = property.minArraySize;  
      
            // Now arraySize returns largeArraySize, and the elements can be retrieved
            [Debug.LogFormat](Debug.LogFormat.html)("New Array Size: {0}, Last element: {1}", property.arraySize, property.GetArrayElementAtIndex(largeArraySize - 1).intValue);
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

