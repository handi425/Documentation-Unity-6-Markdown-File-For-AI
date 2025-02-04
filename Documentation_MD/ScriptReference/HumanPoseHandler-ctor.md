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

# HumanPoseHandler Constructor

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

public HumanPoseHandler([Avatar](Avatar.html) avatar,
[Transform](Transform.html) root);

## Declaration

public HumanPoseHandler([Avatar](Avatar.html) avatar, string[] jointPaths);

### Parameters

avatar | The avatar from which [HumanPose](HumanPose.html) will be read or written. The avatar must be a humanoid.  
---|---  
root | The top most parent of the skeleton hierarchy defined in the humanoid `avatar`. This must match the `avatar` definition.  
jointPaths | A list that defines the `avatar` joint paths. Each joint path starts from the node after the root transform and continues down the avatar skeleton hierarchy. The root transform joint path is an empty string.  
  
### Description

Creates a human pose handler from an `avatar` and a `root` transform and
either a list of joint paths.

Specify an `avatar` and a `root` transform to create a human pose from the
skeleton hierarchy (avatar). Specify an `avatar` and a list of joint paths to
create a human pose handler that is not bound to a skeleton transform
hierarchy. You can use a human pose handler created from joint paths to
convert a human pose to or from an array of local joint transforms
(jointPaths).

    
    
    using UnityEngine;
    using System.Collections;
    using System.Collections.Generic;
    using Unity.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Avatar](Avatar.html) avatar;
        public [Transform](Transform.html) avatarRoot;  
      
        void ParseAvatarTransformRecursive([Transform](Transform.html) t, string parentPath, List<string> jointPaths, List<[Transform](Transform.html)> transforms)
        {
            string jointPath = parentPath.Length == 0 ? t.gameObject.name : parentPath + "/" + t.gameObject.name;
            jointPaths.Add(jointPath);
            transforms.Add(t);  
      
            foreach ([Transform](Transform.html) child in t)
            {
                ParseAvatarTransformRecursive(t, jointPath, jointPaths, transforms);
            }
        }  
      
        void ParseAvatarRootTransform([Transform](Transform.html) rootTransform, List<string> jointPaths, List<[Transform](Transform.html)> transforms)
        {
            jointPaths.Add(""); // root tranform path is the empty string
            transforms.Add(rootTransform);  
      
            foreach ([Transform](Transform.html) t in rootTransform)
            {
                ParseAvatarTransformRecursive(t, "", jointPaths, transforms);
            }
        }  
      
        void Start()
        {
            List<string> jointPaths = new List<string>();
            List<[Transform](Transform.html)> avatarTransforms = new List<[Transform](Transform.html)>();
            ParseAvatarRootTransform(avatarRoot, jointPaths, avatarTransforms);  
      
            [HumanPoseHandler](HumanPoseHandler.html) humanPoseHandler = new [HumanPoseHandler](HumanPoseHandler.html)(avatar, jointPaths.ToArray());
            NativeArray<float> avatarPose = new NativeArray<float>(jointPaths.Count * 7, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));  
      
            for (int i = 0; i < jointPaths.Count; ++i)
            {
                [Vector3](Vector3.html) position = avatarTransforms[i].localPosition;
                [Quaternion](Quaternion.html) rotation = avatarTransforms[i].localRotation;
                avatarPose[7 * i] = position.x;
                avatarPose[7 * i + 1] = position.y;
                avatarPose[7 * i + 2] = position.z;
                avatarPose[7 * i + 3] = rotation.x;
                avatarPose[7 * i + 4] = rotation.y;
                avatarPose[7 * i + 5] = rotation.z;
                avatarPose[7 * i + 6] = rotation.w;
            }  
      
            humanPoseHandler.SetInternalAvatarPose(avatarPose);  
      
            avatarPose.Dispose();
            humanPoseHandler.Dispose();
        }
    }
    

The above example creates a human pose handler from an avatar and a list of
avatar joints. The example reads the pose from the avatar root transform and
writes the pose to the human pose handler.

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

