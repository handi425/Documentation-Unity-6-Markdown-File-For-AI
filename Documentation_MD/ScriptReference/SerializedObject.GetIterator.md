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

#  [SerializedObject](SerializedObject.html).GetIterator

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

public [SerializedProperty](SerializedProperty.html) GetIterator();

### Description

Get the first serialized property.

You can use this to go over all properties of the target object. Typically,
when the desired field name is known, it is better to use
[FindProperty](SerializedObject.FindProperty.html) to retrieve the associated
[SerializedProperty](SerializedProperty.html) more quickly. However this
method can be useful for more general code that needs to scan different types
of objects, e.g. when the names of desired properties is not known in advance.  
  
Additional resources: [FindProperty](SerializedObject.FindProperty.html),
[SerializedProperty.NextVisible](SerializedProperty.NextVisible.html),
[SerializedProperty.Reset](SerializedProperty.Reset.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Text;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class SerializeObjectGetIteratorExample : [ScriptableObject](ScriptableObject.html)
    {
        public bool m_FirstField;  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedObject](SerializedObject.html) GetIterator")]
        static void GetIteratorExample()
        {
            // Each Unity Object has some internal properties that will be serialized.
            // Some of these are visible in the inspector, others are hidden.
            // Typically they can be ignored, but when using [SerializedObject.GetIterator](SerializedObject.GetIterator.html)() they
            // appear prior to the C# fields.
            var scriptableObject = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<SerializeObjectGetIteratorExample>();  
      
            using (var serializedObject = new [SerializedObject](SerializedObject.html)(scriptableObject))
            {
                [SerializedProperty](SerializedProperty.html) iterator = serializedObject.GetIterator();  
      
                var sb = new StringBuilder();
                sb.AppendLine("Visible Internal Properties:");  
      
                // GetIterator returns a root that is above all others (depth -1)
                // so first property is found by stepping into the children
                bool visitChildren = true;
                iterator.NextVisible(visitChildren);  
      
                // For rest of scan stay at the same level (depth 0)
                visitChildren = false;  
      
                do
                {
                    if (iterator.name == "m_FirstField")
                        break; // Found first field from the C# object  
      
                    sb.AppendLine($"\t{iterator.name}");
                }
                while (iterator.NextVisible(visitChildren));  
      
                // [Repeat](UIElements.Repeat.html), using "Next" to show the hidden properties as well as visible
                sb.AppendLine("All Internal Properties:");  
      
                iterator.Reset();
                visitChildren = true;
                iterator.Next(visitChildren);
                visitChildren = false;  
      
                do
                {
                    if (iterator.name == "m_FirstField")
                        break;
                    sb.AppendLine($"\t{iterator.name}");
                }
                while (iterator.Next(visitChildren));  
      
                [Debug.Log](Debug.Log.html)(sb.ToString());
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

