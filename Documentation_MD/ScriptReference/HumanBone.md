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

# HumanBone

struct in UnityEngine

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

The mapping between a bone in the model and the conceptual bone in the Mecanim
human anatomy.

The names of the Mecanim human bone and the bone in the model are stored along
with the limiting muscle values that constrain the bone's rotation during
animation.

    
    
    using UnityEngine;
    using System.Collections.Generic;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            Dictionary<string, string> boneName = new System.Collections.Generic.Dictionary<string, string>();
            boneName["Chest"] = "Bip001 Spine2";
            boneName["Head"] = "Bip001 Head";
            boneName["Hips"] = "Bip001 Pelvis";
            boneName["LeftFoot"] = "Bip001 L Foot";
            boneName["LeftHand"] = "Bip001 L [Hand](XR.Hand.html)";
            boneName["LeftLowerArm"] = "Bip001 L Forearm";
            boneName["LeftLowerLeg"] = "Bip001 L Calf";
            boneName["LeftShoulder"] = "Bip001 L Clavicle";
            boneName["LeftUpperArm"] = "Bip001 L UpperArm";
            boneName["LeftUpperLeg"] = "Bip001 L Thigh";
            boneName["RightFoot"] = "Bip001 R Foot";
            boneName["RightHand"] = "Bip001 R [Hand](XR.Hand.html)";
            boneName["RightLowerArm"] = "Bip001 R Forearm";
            boneName["RightLowerLeg"] = "Bip001 R Calf";
            boneName["RightShoulder"] = "Bip001 R Clavicle";
            boneName["RightUpperArm"] = "Bip001 R UpperArm";
            boneName["RightUpperLeg"] = "Bip001 R Thigh";
            boneName["Spine"] = "Bip001 Spine1";
            string[] humanName = [HumanTrait.BoneName](HumanTrait.BoneName.html);
            [HumanBone](HumanBone.html)[] humanBones = new [HumanBone](HumanBone.html)[boneName.Count];
            int j = 0;
            int i = 0;
            while (i < humanName.Length)
            {
                if (boneName.ContainsKey(humanName[i]))
                {
                    [HumanBone](HumanBone.html) humanBone = new [HumanBone](HumanBone.html)();
                    humanBone.humanName = humanName[i];
                    humanBone.boneName = boneName[humanName[i]];
                    humanBone.limit.useDefaultValues = true;
                    humanBones[j++] = humanBone;
                }
                i++;
            }
        }
    }
    

Additional resources: [HumanDescription](HumanDescription.html),
[AvatarBuilder](AvatarBuilder.html).

### Properties

[boneName](HumanBone-boneName.html)| The name of the bone to which the Mecanim
human bone is mapped.  
---|---  
[humanName](HumanBone-humanName.html)| The name of the Mecanim human bone to
which the bone from the model is mapped.  
[limit](HumanBone-limit.html)| The rotation limits that define the muscle for
this bone.  
  
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

