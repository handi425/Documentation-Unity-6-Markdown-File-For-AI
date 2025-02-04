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

# AnimatorOverrideController

class in UnityEngine

/

Inherits from:[RuntimeAnimatorController](RuntimeAnimatorController.html)

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

Interface to control Animator Override Controller.

Animator Override Controller is used to override Animation Clips from a
controller to specialize animations for a given Avatar. Swapping
[Animator.runtimeAnimatorController](Animator-runtimeAnimatorController.html)
with an [AnimatorOverrideController](AnimatorOverrideController.html) based on
the same [AnimatorController](Animations.AnimatorController.html) at runtime
doesn't reset state machine's current state.  
  
There are three ways to use the Animator Override Controller.  
**1\. Create an Animator Override Controller in the Editor.**  
**2\. Change one Animation Clip per frame at runtime (Basic use case).**  
In this case the indexer operator
[AnimatorOverrideController.this[string]](AnimatorOverrideController.Index_operator.html)
could be used, but be careful as each call will trigger a reallocation of the
animator's clip bindings.

    
    
    using UnityEngine;  
      
    public class SwapWeapon : [MonoBehaviour](MonoBehaviour.html)
    {
        public [AnimationClip](AnimationClip.html)[] weaponAnimationClip;  
      
        protected [Animator](Animator.html) animator;
        protected [AnimatorOverrideController](AnimatorOverrideController.html) animatorOverrideController;  
      
        protected int weaponIndex;  
      
        public void Start()
        {
            animator = GetComponent<[Animator](Animator.html)>();
            weaponIndex = 0;  
      
            animatorOverrideController = new [AnimatorOverrideController](AnimatorOverrideController.html)(animator.runtimeAnimatorController);
            animator.runtimeAnimatorController = animatorOverrideController;
        }  
      
        public void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetButtonDown](Input.GetButtonDown.html)("NextWeapon"))
            {
                weaponIndex = (weaponIndex + 1) % weaponAnimationClip.Length;
                animatorOverrideController["shot"] = weaponAnimationClip[weaponIndex];
            }
        }
    }
    

**3\. Changing many Animation Clips per frame at runtime (Advanced use
case).**  
The
[AnimatorOverrideController.ApplyOverrides](AnimatorOverrideController.ApplyOverrides.html)
method is well suited for this case as it reduce the number of animator's
clips bindings reallocation to only one per call.

    
    
    using UnityEngine;
    using System.Collections.Generic;  
      
    public class AnimationClipOverrides : List<KeyValuePair<[AnimationClip](AnimationClip.html), [AnimationClip](AnimationClip.html)>>
    {
        public AnimationClipOverrides(int capacity) : base(capacity) {}  
      
        public [AnimationClip](AnimationClip.html) this[string name]
        {
            get { return this.Find(x => x.Key.name.Equals(name)).Value; }
            set
            {
                int index = this.FindIndex(x => x.Key.name.Equals(name));
                if (index != -1)
                    this[index] = new KeyValuePair<[AnimationClip](AnimationClip.html), [AnimationClip](AnimationClip.html)>(this[index].Key, value);
            }
        }
    }  
      
    public class Weapon
    {
        public [AnimationClip](AnimationClip.html) singleAttack;
        public [AnimationClip](AnimationClip.html) comboAttack;
        public [AnimationClip](AnimationClip.html) dashAttack;
        public [AnimationClip](AnimationClip.html) smashAttack;
    }  
      
    public class SwapWeapon : [MonoBehaviour](MonoBehaviour.html)
    {
        public Weapon[] weapons;  
      
        protected [Animator](Animator.html) animator;
        protected [AnimatorOverrideController](AnimatorOverrideController.html) animatorOverrideController;  
      
        protected int weaponIndex;  
      
        protected AnimationClipOverrides clipOverrides;
        public void Start()
        {
            animator = GetComponent<[Animator](Animator.html)>();
            weaponIndex = 0;  
      
            animatorOverrideController = new [AnimatorOverrideController](AnimatorOverrideController.html)(animator.runtimeAnimatorController);
            animator.runtimeAnimatorController = animatorOverrideController;  
      
            clipOverrides = new AnimationClipOverrides(animatorOverrideController.overridesCount);
            animatorOverrideController.GetOverrides(clipOverrides);
        }  
      
        public void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetButtonDown](Input.GetButtonDown.html)("NextWeapon"))
            {
                weaponIndex = (weaponIndex + 1) % weapons.Length;
                clipOverrides["SingleAttack"] = weapons[weaponIndex].singleAttack;
                clipOverrides["ComboAttack"] = weapons[weaponIndex].comboAttack;
                clipOverrides["DashAttack"] = weapons[weaponIndex].dashAttack;
                clipOverrides["SmashAttack"] = weapons[weaponIndex].smashAttack;
                animatorOverrideController.ApplyOverrides(clipOverrides);
            }
        }
    }
    

### Properties

[overridesCount](AnimatorOverrideController-overridesCount.html)| Returns the
count of overrides.  
---|---  
[runtimeAnimatorController](AnimatorOverrideController-
runtimeAnimatorController.html)| The Runtime Animator Controller that the
Animator Override Controller overrides.  
[this[string]](AnimatorOverrideController.Index_operator.html)| Returns either
the overriding Animation Clip if set or the original Animation Clip named
name.  
  
### Constructors

[AnimatorOverrideController](AnimatorOverrideController-ctor.html)| Creates an
empty Animator Override Controller.  
---|---  
  
### Public Methods

[ApplyOverrides](AnimatorOverrideController.ApplyOverrides.html)| Applies the
list of overrides on this Animator Override Controller.  
---|---  
[GetOverrides](AnimatorOverrideController.GetOverrides.html)| Gets the list of
Animation Clip overrides currently defined in this Animator Override
Controller.  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
[animationClips](RuntimeAnimatorController-animationClips.html)| Retrieves all
AnimationClip used by the controller.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

