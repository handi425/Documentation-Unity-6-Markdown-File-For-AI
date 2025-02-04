[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-Quaternion.html)
  * [中文](/cn/current/Manual/class-Quaternion.html)
  * [日本語](/ja/current/Manual/class-Quaternion.html)
  * [한국어](/kr/current/Manual/class-Quaternion.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-Quaternion.html)
  * [中文](/cn/current/Manual/class-Quaternion.html)
  * [日本語](/ja/current/Manual/class-Quaternion.html)
  * [한국어](/kr/current/Manual/class-Quaternion.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * Rotation and oriention with quaternion

[](scripting-vectors.html)

Moving objects with vectors

[](class-Mathf.html)

Using common math functions

# Rotation and oriention with quaternion

[Switch to Scripting](../ScriptReference/Quaternion.html "Go to Quaternion
page in the Scripting Reference")

Unity uses the **Quaternion** Unity’s standard way of representing rotations
as data. When writing code that deals with rotations, you should usually use
the Quaternion class and its methods. [More
info](QuaternionAndEulerRotationsInUnity.html)  
See in [Glossary](Glossary.html#Quaternion) class to store the three
dimensional orientation of **GameObjects** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), as well as using them to describe
a relative rotation from one orientation to another.

This page provides an overview of the Quaternion class and its common uses
when scripting with it. For an exhaustive reference of every member of the
Quaternion class, see the [Quaternion script
reference](../ScriptReference/Quaternion.html).

It’s important to understand the difference between Euler angles (the X, Y, &
Z values that you see in the inspector for the rotation of a GameObject), and
the underlying Quaternion value which Unity uses to store the actual rotation
of GameObjects. For the basics of this topic, read [Rotation and Orientation
in Unity](QuaternionAndEulerRotationsInUnity.html).

When dealing with handling rotations in your **scripts** A piece of code that
allows you to create your own Components, trigger game events, modify
Component properties over time and respond to user input in any way you like.
[More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts), you should use the Quaternion class
and its functions to create and modify rotational values. There are some
situations where it is valid to use Euler angles, but you should bear in mind:
\- You should use the Quaternion Class functions that deal with Euler angles
\- Retrieving, modifying, and re-applying Euler values from a rotation can
cause unintentional side-effects (see below)

## Creating and manipulating quaternions directly

Unity’s Quaternion class has a number of functions which allow you to create
and manipulate rotations without needing to use Euler angles at all, and these
are the ones you should use in most typical cases. Each of these links to the
Script Reference with code samples:

### Creating Rotations:

  * [`Quaternion.LookRotation`](../ScriptReference/Quaternion.LookRotation.html)
  * [`Quaternion.Angle`](../ScriptReference/Quaternion.Angle.html)
  * [`Quaternion.AngleAxis`](../ScriptReference/Quaternion.AngleAxis.html)
  * [`Quaternion.FromToRotation`](../ScriptReference/Quaternion.FromToRotation.html)

### Manipulating Rotations:

  * [`Quaternion.Slerp`](../ScriptReference/Quaternion.Slerp.html)
  * [`Quaternion.Inverse`](../ScriptReference/Quaternion.Inverse.html)
  * [`Quaternion.RotateTowards`](../ScriptReference/Quaternion.RotateTowards.html)

The Transform class also provides methods which allow you to work with the
Quaternion rotations:

  * [`Transform.Rotate`](../ScriptReference/Transform.Rotate.html) & [`Transform.RotateAround`](../ScriptReference/Transform.RotateAround.html)

## Working with Euler angles

In some cases it’s more desirable to use Euler angles in your scripts. When
doing so, it’s important to note that you must keep your angles in variables,
and only use them to _apply_ them as Euler angles to your rotation, which
should still ultimately be stored as a Quaternion. While it’s possible to
retrieve Euler angles _from_ a quaternion, if you retrieve, modify and re-
apply, problems are likely to arise.

You can read more detail about exactly how these problems can arise in the
[eulerAngles script reference page](../ScriptReference/Quaternion-
eulerAngles.html).

Here are some examples of **mistakes** commonly made using a hypothetical
example of trying to rotate a GameObject around the X axis at 10 degrees per
second. This is what you should **avoid** :

    
    
    // rotation scripting mistake #1
    // the mistake here is that we are modifying the x value of a quaternion
    // this value does not represent an angle, and does not produce desired results
        
    void Update () 
    {
        var rot = transform.rotation;
        rot.x += Time.deltaTime * 10;
        transform.rotation = rot;
    }
    
    
    
    // rotation scripting mistake #2
    // Read, modify, then write the Euler values from a Quaternion.
    // Because these values are calculated from a Quaternion,
    // each new rotation might return very different Euler angles, which might suffer from gimbal lock.
            
    void Update () 
    {
        var angles = transform.rotation.eulerAngles;
        angles.x += Time.deltaTime * 10;
        transform.rotation = Quaternion.Euler(angles);
    }
    

And here is an example of using Euler angles in script **correctly** :

    
    
    // Rotation scripting with Euler angles correctly.
    // Store the Euler angle in a class variable, and only use it to
    // apply it as an Euler angle, but never rely on reading the Euler back.
            
    float x;
    void Update () 
    {
        x += Time.deltaTime * 10;
        transform.rotation = Quaternion.Euler(x,0,0);
    }
    

## Additional resources

  * [Rotation and orientation in Unity](QuaternionAndEulerRotationsInUnity.html)
  * [Quaternion API reference](../ScriptReference/Quaternion.html)

[](scripting-vectors.html)

Moving objects with vectors

[](class-Mathf.html)

Using common math functions

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

