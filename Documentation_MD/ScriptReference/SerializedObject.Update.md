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

#  [SerializedObject](SerializedObject.html).Update

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

public void Update();

### Description

Update serialized object's representation.

When a SerializedObject is constructed, the target objects are serialized, and
the SerializeObject and SerializedProperty API provide read and write access
to that serialized representation. If one or more of the target objects are
changed, via another SerializedObject instance or direct writes to the target
objects, then the SerializedObject internal serialized representation can get
out of sync. Calling Update() will reserialize the target objects so that the
SerializedObject reflects their latest state.  
  
Calling Update() will discard any locally modified properties that have not
yet been applied.  
  
Additional resources:
[SerializedObject.hasModifiedProperties](SerializedObject-
hasModifiedProperties.html),
[SerializedObject.ApplyModifiedProperties](SerializedObject.ApplyModifiedProperties.html)

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Text;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class SerializeObjectUpdate : [ScriptableObject](ScriptableObject.html)
    {
        public int m_Field = 1;  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedObject](SerializedObject.html) [Update](PlayerLoop.Update.html)")]
        static void UpdateExample()
        {
            var scriptableObject = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<SerializeObjectUpdate>();
            var sb = new StringBuilder();  
      
            using (var serializedObject = new [SerializedObject](SerializedObject.html)(scriptableObject))
            {
                [SerializedProperty](SerializedProperty.html) field = serializedObject.FindProperty("m_Field");  
      
                // Change underlying object
                scriptableObject.m_Field = 2;  
      
                // [SerializedObject](SerializedObject.html) still thinks value is 1
                sb.Append($"[SerializedObject](SerializedObject.html) value before [Update](PlayerLoop.Update.html): {field.intValue} ");  
      
                //hasModifiedProperties returns false because no changes have been made via [SerializedProperty](SerializedProperty.html) API
                sb.Append($"([SerializedObject](SerializedObject.html) dirty: {serializedObject.hasModifiedProperties}), ");  
      
                // [Update](PlayerLoop.Update.html) so that [SerializedObject](SerializedObject.html) sees the new value
                serializedObject.Update();
                sb.AppendLine($"after [Update](PlayerLoop.Update.html): {field.intValue}");  
      
                // Another scenario is when [Update](PlayerLoop.Update.html) is called while there are pending changes in the [SerializedObject](SerializedObject.html)
                field.intValue = 3;
                sb.Append($"[SerializedObject](SerializedObject.html) value before [Update](PlayerLoop.Update.html): {field.intValue} ");
                sb.Append($"([SerializedObject](SerializedObject.html) dirty: {serializedObject.hasModifiedProperties}), ");  
      
                // Value reverts back to 2, because ApplyModifiedProperties was not called
                // and [SerializedObject](SerializedObject.html) has been put back in sync with the object's state
                serializedObject.Update();
                sb.AppendLine($"after [Update](PlayerLoop.Update.html): {field.intValue}. (Dirty: {serializedObject.hasModifiedProperties})");  
      
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

