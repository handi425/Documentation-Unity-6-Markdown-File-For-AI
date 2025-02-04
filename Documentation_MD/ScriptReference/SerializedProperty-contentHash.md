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

#  [SerializedProperty](SerializedProperty.html).contentHash

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

public uint contentHash;

### Description

Provides the hash value for the property. (Read Only)

You can use this to track if there has been any changes to the value at the
property path (Additional resources:
[SerializedProperty.propertyPath](SerializedProperty-propertyPath.html)).  
  
Please note that:  
-If the size of the property's content is smaller than or equal to 32 bits, then the content will be returned instead of a hash.   
-If the property path leads to an array or complex type, the hash will correspond to the entire content.   
-If the property is a field with [SerializeReference] attribute, or a compound type that contains such a field, then the content hashing doesn't include the content of the referenced object, instead it only hashes the reference id (Additional resources: [SerializedProperty.managedReferenceId](SerializedProperty-managedReferenceId.html)).
    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class MyObject : [ScriptableObject](ScriptableObject.html)
    {
        public string myString = "answer to life the universe and everything";
        public string[] myStringArray = { "answer", "to", "life", "the", "universe", "and", "everything" };
        public int[] myIntArray = { 42, 442, 422, 4242 };  
      
        [[MenuItem](MenuItem.html)("Example/Output contentHash from [SerializedProperty](SerializedProperty.html)")]
        static void OutputContentHashFromSerializedProperty()
        {
            var scriptableObject = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<MyObject>();  
      
            using (var serializedObject = new [SerializedObject](SerializedObject.html)(scriptableObject))
            {
                [SerializedProperty](SerializedProperty.html) serializedPropertyMyString = serializedObject.FindProperty("myString");
                [SerializedProperty](SerializedProperty.html) serializedPropertyMyStringArray = serializedObject.FindProperty("myStringArray");
                [SerializedProperty](SerializedProperty.html) serializedPropertyMyIntArray = serializedObject.FindProperty("myIntArray");  
      
                uint myStringHash = serializedPropertyMyString.contentHash;
                uint myStringArrayHash = serializedPropertyMyStringArray.contentHash;
                uint MyIntArrayHash = serializedPropertyMyIntArray.contentHash;  
      
                serializedPropertyMyString.stringValue = "new string";
                serializedPropertyMyIntArray.DeleteArrayElementAtIndex(1);  
      
                serializedObject.ApplyModifiedPropertiesWithoutUndo();  
      
                [Debug.Log](Debug.Log.html)(string.Format("myString: before={0}, after={1}, changed={2}", myStringHash, serializedPropertyMyString.contentHash, myStringHash == serializedPropertyMyString.contentHash ? "no" : "yes"));
                [Debug.Log](Debug.Log.html)(string.Format("myStringArrayHash: before={0}, after={1}, changed={2}", myStringArrayHash, serializedPropertyMyStringArray.contentHash, myStringArrayHash == serializedPropertyMyStringArray.contentHash ? "no" : "yes"));
                [Debug.Log](Debug.Log.html)(string.Format("MyIntArrayHash: before={0}, after={1}, changed={2}", MyIntArrayHash, serializedPropertyMyIntArray.contentHash, MyIntArrayHash == serializedPropertyMyIntArray.contentHash ? "no" : "yes"));
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

