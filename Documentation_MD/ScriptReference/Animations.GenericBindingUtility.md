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

# GenericBindingUtility

class in UnityEngine.Animations

/

Implemented in:[UnityEngine.AnimationModule](UnityEngine.AnimationModule.html)

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

### Description

Animation utility functions for reading and writing values from Unity
components.

    
    
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.Animations;
    using [UnityEditor](UnityEditor.html);
    using Unity.Collections;
    using System.Linq;  
      
    public class AnimationClipPlayer : [MonoBehaviour](MonoBehaviour.html)
    {
        public [AnimationClip](AnimationClip.html)        animationClip;
        public float                time;  
      
        List<[AnimationCurve](AnimationCurve.html)>        curves;  
      
        NativeArray<[BoundProperty](Animations.BoundProperty.html)>  floatProperties;
        NativeArray<[BoundProperty](Animations.BoundProperty.html)>  intProperties;
        NativeArray<float>          floatValues;
        NativeArray<int>            intValues;  
      
        void Start()
        {
            var editorCurveBindings = [AnimationUtility.GetCurveBindings](AnimationUtility.GetCurveBindings.html)(animationClip);
            editorCurveBindings = editorCurveBindings.Where(editorCurveBinding =>
                editorCurveBinding.type != typeof([Transform](Transform.html)) && !editorCurveBinding.isPPtrCurve && !editorCurveBinding.isDiscreteCurve
                ).ToArray();  
      
            curves = new List<[AnimationCurve](AnimationCurve.html)>(editorCurveBindings.Length);
            for (var i = 0; i < editorCurveBindings.Length; i++)
            {
                curves.Add([AnimationUtility.GetEditorCurve](AnimationUtility.GetEditorCurve.html)(animationClip, editorCurveBindings[i]));
            }  
      
            var genericBindings = new NativeArray<[GenericBinding](Animations.GenericBinding.html)>([AnimationUtility.EditorCurveBindingsToGenericBindings](AnimationUtility.EditorCurveBindingsToGenericBindings.html)(editorCurveBindings), [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            [GenericBindingUtility.BindProperties](Animations.GenericBindingUtility.BindProperties.html)(gameObject, genericBindings, out floatProperties, out intProperties, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));  
      
            floatValues = new NativeArray<float>(floatProperties.Length, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
            intValues = new NativeArray<int>(intProperties.Length, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
        }  
      
        private void OnDestroy()
        {
            floatProperties.Dispose();
            floatValues.Dispose();
            intProperties.Dispose();
            intValues.Dispose();
        }  
      
        // [Update](PlayerLoop.Update.html) is called once per frame
        void [Update](PlayerLoop.Update.html)()
        {
            for (int i = 0; i < curves.Count; i++)
            {
                floatValues[i] = curves[i].Evaluate(time);
            }  
      
            [GenericBindingUtility.SetValues](Animations.GenericBindingUtility.SetValues.html)(floatProperties, floatValues);
        }
    }
    

### Static Methods

[BindProperties](Animations.GenericBindingUtility.BindProperties.html)|
Retrieves the list of BoundProperty defined by the list of GenericBinding.  
---|---  
[CreateGenericBinding](Animations.GenericBindingUtility.CreateGenericBinding.html)|
Retrieves the GenericBinding that represents a specific property associated
with a GameObject or one of its components.  
[GetAnimatableBindings](Animations.GenericBindingUtility.GetAnimatableBindings.html)|
Retrieves the animatable bindings for a specific GameObject.  
[GetCurveBindings](Animations.GenericBindingUtility.GetCurveBindings.html)|
Retrieves the curve bindings from an animation clip.  
[GetValues](Animations.GenericBindingUtility.GetValues.html)| Retrieves the
float or integer value for each [[BoundProperty].  
[SetValues](Animations.GenericBindingUtility.SetValues.html)| Sets the float
or integer value for each [[BoundProperty].  
[UnbindProperties](Animations.GenericBindingUtility.UnbindProperties.html)|
Unbinds and frees all resources used by a list of BoundProperty.  
  
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

