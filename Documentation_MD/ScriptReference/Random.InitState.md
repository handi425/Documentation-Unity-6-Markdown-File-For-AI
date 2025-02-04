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

#  [Random](Random.html).InitState

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

[Switch to Manual](../Manual/class-random.html "Go to Random Component in the
Manual")

## Declaration

public static void InitState(int seed);

### Parameters

seed | Seed used to initialize the random number generator.  
---|---  
  
### Description

Initializes the random number generator state with a seed.

The random number generator is not truly random, but produces numbers in a
preset sequence (the values in the sequence "jump" around the range in such a
way that they appear random for most purposes).  
  
The point in the sequence where a particular run of pseudo-random values
begins is selected using an integer called the _seed_ value. This prevents the
same run of values from occurring each time a game is played and thus avoids
predictable gameplay. It is sometimes useful to produce the same run of
pseudo-random values on demand by setting the seed yourself.  
  
You might set your own seed, for example, when you generate a game level
procedurally. You can use randomly-chosen elements to make the Scene look
arbitrary and natural but set the seed to a preset value before generating.
This will make sure that the same "random" pattern is produced each time the
game is played. This can often be an effective way to reduce a game's storage
requirements - you can generate as many levels as you like procedurally and
store each one using nothing more than an integer seed value.  
  
The seed is randomly initialized at startup (see [Random](Random.html) for
more information on this) but if you want to randomize it later on, you can
use `Random.InitState((int)DateTime.Now.Ticks)`.  
  
The seed cannot be retrieved once set - the pseudorandomization algorithm
stores its internal state in a more complex set of numbers. However, this
state can be loaded and stored via the [state](Random-state.html) property,
which works with the opaque but serializable [State](Random.State.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private float[] noiseValues;
        void Start()
        {
            [Random.InitState](Random.InitState.html)(42);
            noiseValues = new float[10];
            for (int i = 0; i < noiseValues.Length; i++)
            {
                noiseValues[i] = [Random.value](Random-value.html);
                [Debug.Log](Debug.Log.html)(noiseValues[i]);
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

