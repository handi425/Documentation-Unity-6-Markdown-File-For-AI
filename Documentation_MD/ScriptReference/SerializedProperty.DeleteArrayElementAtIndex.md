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

#  [SerializedProperty](SerializedProperty.html).DeleteArrayElementAtIndex

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

public void DeleteArrayElementAtIndex(int index);

### Description

Delete the element at the specified index in the array.

Additional resources: [isArray](SerializedProperty-isArray.html),
[InsertArrayElementAtIndex](SerializedProperty.InsertArrayElementAtIndex.html),
[MoveArrayElement](SerializedProperty.MoveArrayElement.html),
[DeleteCommand](SerializedProperty.DeleteCommand.html).

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class DeleteArrayElementAtIndexExample : [ScriptableObject](ScriptableObject.html)
    {
        public List<string> m_Data;  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedProperty](SerializedProperty.html)/DeleteArrayElementAtIndex Example")]
        static void MenuCallback()
        {
            DeleteArrayElementAtIndexExample obj = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<DeleteArrayElementAtIndexExample>();
            obj.m_Data = new List<string>() { "The", "big", "cat", "jumped." };  
      
            [SerializedObject](SerializedObject.html) serializedObject = new [SerializedObject](SerializedObject.html)(obj);
            [SerializedProperty](SerializedProperty.html) arrayProperty = serializedObject.FindProperty("m_Data");  
      
            arrayProperty.DeleteArrayElementAtIndex(1);  
      
            // With previous deletion index 2 now becomes the last element
            arrayProperty.DeleteArrayElementAtIndex(2);  
      
            serializedObject.ApplyModifiedProperties();  
      
            // Outputs "The cat"
            [Debug.Log](Debug.Log.html)("Final array contents: " + string.Join(" ", obj.m_Data));
        }
    }
    
    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class DeleteArrayElementAtIndexExample2 : [ScriptableObject](ScriptableObject.html)
    {
        public int[] m_Array = new int[] { 1, -1, -1, 3, -1, -1, 1, 3, -1 };  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedProperty](SerializedProperty.html)/DeleteArrayElementAtIndex Example 2")]
        static void MenuCallback()
        {
            var scriptableObject = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<DeleteArrayElementAtIndexExample2>();  
      
            using (var serializedObject = new [SerializedObject](SerializedObject.html)(scriptableObject))
            {
                [SerializedProperty](SerializedProperty.html) arrayProperty = serializedObject.FindProperty("m_Array");  
      
                // Iterate the array removing any negative numbers
                int arraySize = arrayProperty.arraySize;
                for (int index = 0; index < arraySize;)
                {
                    var arrayElement = arrayProperty.GetArrayElementAtIndex(index);
                    if (arrayElement.intValue < 0)
                    {
                        arrayProperty.DeleteArrayElementAtIndex(index);
                        arraySize--;
                    }
                    else
                    {
                        index++;
                    }
                }  
      
                serializedObject.ApplyModifiedProperties();
                [Debug.Log](Debug.Log.html)("Cleaned array contents: " + string.Join(" ", scriptableObject.m_Array));
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

