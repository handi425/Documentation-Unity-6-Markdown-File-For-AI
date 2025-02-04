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

#  [Undo](Undo.html).RecordObject

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

public static void RecordObject([Object](Object.html) objectToUndo, string
name);

### Parameters

objectToUndo | The reference to the object that you will be modifying.  
---|---  
name | The title of the action to appear in the undo history (i.e. visible in the undo menu).  
  
### Description

Records any changes done on the object after the RecordObject function.

Almost all property changes can be recorded with this function. The transform
parent, AddComponent, object destruction can not be recorded with this
function, for that you should use the dedicated functions.  
  
Internally this creates a temporary copy of the object's state. At the end of
the frame Unity diffs the state and detects what has changed. The changed
properties are recorded on the undo stack. If nothing has changed (Binary
exact comparison is used for all properties), no undo operations are stored on
the stack.  
  
**Important:** To correctly handle instances where _objectToUndo_ is an
instance of a Prefab,
[PrefabUtility.RecordPrefabInstancePropertyModifications](PrefabUtility.RecordPrefabInstancePropertyModifications.html)
must be called after RecordObject.  
  
This is an example of an editor script which allows you to change an effect
radius variable. The Undo state is recorded, allowing you to revert the change
using the undo system.

    
    
    //Name this script "EffectRadiusEditor"
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    [[CustomEditor](CustomEditor.html)(typeof(EffectRadius))]
    public class EffectRadiusEditor : [Editor](Editor.html)
    {
        public void OnSceneGUI()
        {
            EffectRadius t = (target as EffectRadius);  
      
            // The Begin and EndChangeChecks check for changes in the [GUI](GUI.html) state. This is not required for
            // [Undo.RecordObject](Undo.RecordObject.html). [Undo.RecordObject](Undo.RecordObject.html) only registers changes to the target
            // after the call to [Undo.RecordObject](Undo.RecordObject.html).
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
            float areaOfEffect = [Handles.RadiusHandle](Handles.RadiusHandle.html)([Quaternion.identity](Quaternion-identity.html), t.transform.position, t.areaOfEffect);
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                [Undo.RecordObject](Undo.RecordObject.html)(target, "Changed Area Of Effect");
                t.areaOfEffect = areaOfEffect;
            }
        }
    }
    

Place this script on a GameObject to see the area of effect handle, and change
the value using the gizmo in the Scene view.

    
    
    //Name this script "EffectRadius"
    using UnityEngine;
    using System.Collections;  
      
    public class EffectRadius : [MonoBehaviour](MonoBehaviour.html)
    {
        public float areaOfEffect = 1;
    }
    

Additional resources: [Undo.RecordObjects](Undo.RecordObjects.html).

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

