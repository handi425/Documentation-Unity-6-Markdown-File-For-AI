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

#  [SerializedProperty](SerializedProperty.html).DeleteCommand

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

public bool DeleteCommand();

### Description

Deletes the array element referenced by the SerializedProperty.

The serialized property can't be used anymore after calling this function. A
new iterator must be created in that case.  
  
Additional resources:
[DeleteArrayElementAtIndex](SerializedProperty.DeleteArrayElementAtIndex.html)

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class SerializePropertyDeleteCommandExample : [ScriptableObject](ScriptableObject.html)
    {
        public int[] m_Array = new int[] { 1, -1, -1, 3, -1, -1, 1, 3, -1 };  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedProperty](SerializedProperty.html)/DeleteCommand Example")]
        static void MenuCallback()
        {
            var scriptableObject = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<SerializePropertyDeleteCommandExample>();  
      
            using (var serializedObject = new [SerializedObject](SerializedObject.html)(scriptableObject))
            {
                [SerializedProperty](SerializedProperty.html) arrayProperty = serializedObject.FindProperty("m_Array");  
      
                int remaining = arrayProperty.arraySize;
                var arrayElement = remaining > 0 ? arrayProperty.GetArrayElementAtIndex(0) : null;
                while (remaining > 0)
                {
                    if (arrayElement.intValue < 0)
                    {
                        // Use a copy of the [SerializedProperty](SerializedProperty.html) because it cannot be used after DeleteCommand is invoked.
                        var elementToDelete = arrayElement.Copy();
                        elementToDelete.DeleteCommand();  
      
                        // The next element, if any, is now at the index of the deleted item, and arrayElement
                        // automatically points at it, hence we don't have to move ahead
                    }
                    else
                    {
                        arrayElement.Next(false);
                    }
                    --remaining;
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

