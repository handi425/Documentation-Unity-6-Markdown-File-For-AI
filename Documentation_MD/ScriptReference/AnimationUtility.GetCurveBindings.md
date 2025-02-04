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

#  [AnimationUtility](AnimationUtility.html).GetCurveBindings

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

public static EditorCurveBinding[]
GetCurveBindings([AnimationClip](AnimationClip.html) clip);

### Description

Retrieves the float curve bindings in an animation clip.

Unity has two types of animation: float curve and object reference curve. A
float curve is a classic curve that animates a float property over time. An
object reference curve is a construct that animates an object reference
property over time.  
  
This method returns the float curve bindings. See
[AnimationUtility.GetObjectReferenceCurveBindings](AnimationUtility.GetObjectReferenceCurveBindings.html)
for object reference curves.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    // [Editor](Editor.html) window for listing all float curves in an animation clip
    public class ClipInfo : [EditorWindow](EditorWindow.html)
    {
        private [AnimationClip](AnimationClip.html) clip;  
      
        [[MenuItem](MenuItem.html)("Window/Clip Info")]
        static void Init()
        {
            GetWindow(typeof(ClipInfo));
        }  
      
        public void OnGUI()
        {
            clip = [EditorGUILayout.ObjectField](EditorGUILayout.ObjectField.html)("Clip", clip, typeof([AnimationClip](AnimationClip.html)), false) as [AnimationClip](AnimationClip.html);  
      
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("Curves:");
            if (clip != null)
            {
                foreach (var binding in [AnimationUtility.GetCurveBindings](AnimationUtility.GetCurveBindings.html)(clip))
                {
                    [AnimationCurve](AnimationCurve.html) curve = [AnimationUtility.GetEditorCurve](AnimationUtility.GetEditorCurve.html)(clip, binding);
                    [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)(binding.path + "/" + binding.propertyName + ", Keys: " + curve.keys.Length);
                }
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

