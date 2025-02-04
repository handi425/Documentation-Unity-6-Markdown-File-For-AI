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

#  [SerializedProperty](SerializedProperty.html).arraySize

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

public int arraySize;

### Description

The number of elements in the array.

If the SerializedObject contains a single object, this property returns the
number of elements in the array.  
  
If the SerializedObject contains multiple objects, this property returns the
smallest number of elements. This is done so that iteration of the
SerializedObject only exposes properties found in all objects.  
  
If there are multiple objects and the smallest array size is larger than
[SerializedObject.maxArraySizeForMultiEditing](SerializedObject-
maxArraySizeForMultiEditing.html) then this property returns 0 and the
elements cannot be retrieved with
[SerializedProperty.GetArrayElementAtIndex](SerializedProperty.GetArrayElementAtIndex.html).  
  
Setting this property to a size smaller than the current size discards
elements from the end, retaining the existing element content for the
remaining elements. Setting this property to a larger size increases the array
size by appending new elements at the end. The values of those new elements
are undefined until explicitly assigned some desired content, as demonstrated
in the second example below.  
  
Additional resources: [isArray](SerializedProperty-isArray.html),
[minArraySize](SerializedProperty-minArraySize.html),
[GetArrayElementAtIndex](SerializedProperty.GetArrayElementAtIndex.html),
[InsertArrayElementAtIndex](SerializedProperty.InsertArrayElementAtIndex.html),
[DeleteArrayElementAtIndex](SerializedProperty.DeleteArrayElementAtIndex.html),
[ClearArray](SerializedProperty.ClearArray.html),
[SerializedObject.targetObjects](SerializedObject-targetObjects.html).

    
    
    using System.Collections.Generic;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class SerializePropertyArraySizeExample : [ScriptableObject](ScriptableObject.html)
    {
        public List<string> m_ListOfStrings = new List<string> { "zero", "one", "two" };
        public string m_NotInArray = "blah";  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedProperty](SerializedProperty.html)/ArraySize Example")]
        static void ArraySizeExample()
        {
            var scriptableObject = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<SerializePropertyArraySizeExample>();  
      
            using (var serializedObject = new [SerializedObject](SerializedObject.html)(scriptableObject))
            {
                var arrayProperty = serializedObject.FindProperty("m_ListOfStrings");
                var arraySize = arrayProperty.arraySize;
                var arrayElement = arrayProperty.GetArrayElementAtIndex(0);  
      
                var concatenated = "Combined array contents: ";
                for (int i = 0; i < arraySize; i++, arrayElement.Next(false))
                {
                    concatenated += arrayElement.stringValue + " ";
                }
                [Debug.Log](Debug.Log.html)(concatenated);
            }
        }
    }
    
    
    
    using System.Collections.Generic;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class SerializePropertyArrayResizeExample : [ScriptableObject](ScriptableObject.html)
    {
        public List<string> m_ListOfStrings;  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedProperty](SerializedProperty.html)/ArraySize Example 2")]
        static void MenuCallback()
        {
            var scriptableObject = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<SerializePropertyArrayResizeExample>();  
      
            using (var serializedObject = new [SerializedObject](SerializedObject.html)(scriptableObject))
            {
                var arrayProperty = serializedObject.FindProperty("m_ListOfStrings");  
      
                // Allocate an initial size of the array
                arrayProperty.arraySize = 2;  
      
                // Set the desired initial content for the new elements
                arrayProperty.GetArrayElementAtIndex(0).stringValue = "zero";
                arrayProperty.GetArrayElementAtIndex(1).stringValue = "one";  
      
                // Append another element
                arrayProperty.arraySize++;
                arrayProperty.GetArrayElementAtIndex(arrayProperty.arraySize - 1).stringValue = "two";  
      
                serializedObject.ApplyModifiedProperties();
                [Debug.Log](Debug.Log.html)("Combined array contents: " + string.Join(" ", scriptableObject.m_ListOfStrings));
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

