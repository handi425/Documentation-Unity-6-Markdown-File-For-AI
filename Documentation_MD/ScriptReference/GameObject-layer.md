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

#  [GameObject](GameObject.html).layer

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

[Switch to Manual](../Manual/class-GameObject.html "Go to GameObject Component
in the Manual")

public int layer;

### Description

Integer identifying the layer the GameObject is assigned to.

This is the standard integer value which identifies the layer, not the
[LayerMask](LayerMask.html). You can use layers for selective rendering from
cameras or to ignore Raycasts. Unity generates 32 layers, identified by
standard integers from 0 to 31, and reserves some layers for its own systems.
Refer to [ Create functional layers in Unity](../Manual/create-layers.html)
for a list of predefined layers and how to create your own new ones.  
  
To convert this `layer` identifier to a [LayerMask](LayerMask.html), refer to
[ Set a layerMask](../Manual/layermask-set.html). To obtain the `string` name
of the layer from this `layer` identifier, use
[LayerMask.LayerToName](LayerMask.LayerToName.html). Refer to
[Layers](../Manual/Layers.html) in the Manual for a comprehensive guide to
using layers.

    
    
    // Put the [GameObject](GameObject.html) in the ignore raycast layer (2)  
      
    using UnityEngine;  
      
    [[ExecuteInEditMode](ExecuteInEditMode.html)]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Awake()
        {
            //gameObject.layer uses only integers, but we can turn a layer name into a layer integer using [LayerMask.NameToLayer](LayerMask.NameToLayer.html)()
            int LayerIgnoreRaycast = [LayerMask.NameToLayer](LayerMask.NameToLayer.html)("Ignore Raycast");
            gameObject.layer = LayerIgnoreRaycast;
            [Debug.Log](Debug.Log.html)("Current layer: " + gameObject.layer);
        }
    }
    

Additional resources: [LayerMask](LayerMask.html)

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

