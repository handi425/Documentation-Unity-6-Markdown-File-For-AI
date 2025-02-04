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

# ParticleSystemForceField

class in UnityEngine

/

Inherits from:[Behaviour](Behaviour.html)

/

Implemented
in:[UnityEngine.ParticleSystemModule](UnityEngine.ParticleSystemModule.html)

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

[Switch to Manual](../Manual/class-ParticleSystemForceField.html "Go to
ParticleSystemForceField Component in the Manual")

### Description

Script interface for Particle System Force Fields.

Particle System Force Fields can be used to influence groups of particles that
enter each field's zone of influence.  
  
The shape of the Force Field can be set to a variety of shapes, and how the
particles are affected is controlled by various properties in the Force Field.  
  
As part of choosing the shape, you may define a start and end range. The end
range describes the maximum extent of the shape, and the start range can be
used to create a hollow shape.  
  
A number of forces can be applied to particles that are within this volume:
directional, gravitational, rotational, drag, and a vector field.  
  
The settings for each type of force make use of the
[MinMaxCurve](ParticleSystem.MinMaxCurve.html) type, which is also used in the
Particle System. This type allows you to set simple uniform values, or more
complicated values that vary per-particle, and vary over the lifetime of each
particle.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections;
    using System.Collections.Generic;
    using System.Linq;
    using UnityEngine;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [ParticleSystemForceFieldShape](ParticleSystemForceFieldShape.html) m_Shape = [ParticleSystemForceFieldShape.Sphere](ParticleSystemForceFieldShape.Sphere.html);
        public float m_StartRange = 0.0f;
        public float m_EndRange = 3.0f;
        public [Vector3](Vector3.html) m_Direction = [Vector3.zero](Vector3-zero.html);
        public float m_Gravity = 0.0f;
        public float m_GravityFocus = 0.0f;
        public float m_RotationSpeed = 0.0f;
        public float m_RotationAttraction = 0.0f;
        public [Vector2](Vector2.html) m_RotationRandomness = [Vector2.zero](Vector2-zero.html);
        public float m_Drag = 0.0f;
        public bool m_MultiplyDragByParticleSize = false;
        public bool m_MultiplyDragByParticleVelocity = false;  
      
        private [ParticleSystemForceField](ParticleSystemForceField.html) m_ForceField;  
      
        void Start()
        {
            // Create a Force Field
            var go = new [GameObject](GameObject.html)("ForceField", typeof([ParticleSystemForceField](ParticleSystemForceField.html)));
            go.transform.position = new [Vector3](Vector3.html)(0, 2, 0);
            go.transform.rotation = [Quaternion.Euler](Quaternion.Euler.html)(new [Vector3](Vector3.html)(90.0f, 0.0f, 0.0f));  
      
            m_ForceField = go.GetComponent<[ParticleSystemForceField](ParticleSystemForceField.html)>();  
      
            // Configure [Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html)
            transform.position = new [Vector3](Vector3.html)(0, -4, 0);
            transform.rotation = [Quaternion.identity](Quaternion-identity.html);
            var ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            var main = ps.main;
            main.startSize = new [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html)(0.05f, 0.2f);
            main.startSpeed = new [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html)(1.5f, 2.5f);
            main.maxParticles = 100000;  
      
            var emission = ps.emission;
            emission.rateOverTime = 0.0f;
            emission.burstCount = 1;
            emission.SetBurst(0, new [ParticleSystem.Burst](ParticleSystem.Burst.html)(0.0f, 200, 200, -1, 0.1f));  
      
            var shape = ps.shape;
            shape.shapeType = [ParticleSystemShapeType.SingleSidedEdge](ParticleSystemShapeType.SingleSidedEdge.html);
            shape.radius = 5.0f;
            shape.radiusMode = [ParticleSystemShapeMultiModeValue.BurstSpread](ParticleSystemShapeMultiModeValue.BurstSpread.html);
            shape.randomPositionAmount = 0.1f;
            shape.randomDirectionAmount = 0.05f;  
      
            var forces = ps.externalForces;
            forces.enabled = true;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            m_ForceField.shape = m_Shape;
            m_ForceField.startRange = m_StartRange;
            m_ForceField.endRange = m_EndRange;
            m_ForceField.directionX = m_Direction.x;
            m_ForceField.directionY = m_Direction.y;
            m_ForceField.directionZ = m_Direction.z;
            m_ForceField.gravity = m_Gravity;
            m_ForceField.gravityFocus = m_GravityFocus;
            m_ForceField.rotationSpeed = m_RotationSpeed;
            m_ForceField.rotationAttraction = m_RotationAttraction;
            m_ForceField.rotationRandomness = m_RotationRandomness;
            m_ForceField.drag = m_Drag;
            m_ForceField.multiplyDragByParticleSize = m_MultiplyDragByParticleSize;
            m_ForceField.multiplyDragByParticleVelocity = m_MultiplyDragByParticleVelocity;
        }  
      
        void OnGUI()
        {
            [GUIContent](GUIContent.html)[] shapeLabels = Enum.GetNames(typeof([ParticleSystemForceFieldShape](ParticleSystemForceFieldShape.html))).Select(n => new [GUIContent](GUIContent.html)(n)).ToArray();
            m_Shape = ([ParticleSystemForceFieldShape](ParticleSystemForceFieldShape.html))[GUI.SelectionGrid](GUI.SelectionGrid.html)(new [Rect](Rect.html)(25, 25, 400, 25), (int)m_Shape, shapeLabels, 4);  
      
            float y = 80.0f;
            float spacing = 40.0f;  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Start Range");
            m_StartRange = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), m_StartRange, 0.0f, 2.0f);
            y += spacing;  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "End Range");
            m_EndRange = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), m_EndRange, 2.0f, 3.0f);
            y += spacing;  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "[Direction](UIElements.NavigationMoveEvent.Direction.html)");
            m_Direction.x = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 40, 30), m_Direction.x, -1.0f, 1.0f);
            m_Direction.y = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(210, y + 5, 40, 30), m_Direction.y, -1.0f, 1.0f);
            m_Direction.z = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(255, y + 5, 40, 30), m_Direction.z, -1.0f, 1.0f);
            y += spacing;  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "[Gravity](Unity.Android.Gradle.Manifest.Gravity.html)");
            m_Gravity = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), m_Gravity, -0.05f, 0.05f);
            y += spacing;  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "[Gravity](Unity.Android.Gradle.Manifest.Gravity.html) Focus");
            m_GravityFocus = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), m_GravityFocus, 0.0f, 1.0f);
            y += spacing;  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Rotation Speed");
            m_RotationSpeed = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), m_RotationSpeed, -10.0f, 10.0f);
            y += spacing;  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Rotation Attraction");
            m_RotationAttraction = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), m_RotationAttraction, 0.0f, 0.01f);
            y += spacing;  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Rotation Randomness");
            m_RotationRandomness.x = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 60, 30), m_RotationRandomness.x, 0.0f, 1.0f);
            m_RotationRandomness.y = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(230, y + 5, 60, 30), m_RotationRandomness.y, 0.0f, 1.0f);
            y += spacing;  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Drag");
            m_Drag = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), m_Drag, 0.0f, 20.0f);
            y += spacing;  
      
            m_MultiplyDragByParticleSize = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, y, 220, 30), m_MultiplyDragByParticleSize, "Multiply Drag by [Particle](ParticleSystem.Particle.html) Size");
            y += spacing;  
      
            m_MultiplyDragByParticleVelocity = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, y, 220, 30), m_MultiplyDragByParticleVelocity, "Multiply Drag by [Particle](ParticleSystem.Particle.html) Velocity");
            y += spacing;
        }
    }
    

### Properties

[directionX](ParticleSystemForceField-directionX.html)| Apply a linear force
along the local X axis to particles within the volume of the Force Field.  
---|---  
[directionY](ParticleSystemForceField-directionY.html)| Apply a linear force
along the local Y axis to particles within the volume of the Force Field.  
[directionZ](ParticleSystemForceField-directionZ.html)| Apply a linear force
along the local Z axis to particles within the volume of the Force Field.  
[drag](ParticleSystemForceField-drag.html)| Apply drag to particles within the
volume of the Force Field.  
[endRange](ParticleSystemForceField-endRange.html)| Determines the size of the
shape used for influencing particles.  
[gravity](ParticleSystemForceField-gravity.html)| Apply gravity to particles
within the volume of the Force Field.  
[gravityFocus](ParticleSystemForceField-gravityFocus.html)| When using the
gravity force, set this value between 0 and 1 to control the focal point of
the gravity effect.  
[length](ParticleSystemForceField-length.html)| Describes the length of the
Cylinder when using the Cylinder Force Field shape to influence particles.  
[multiplyDragByParticleSize](ParticleSystemForceField-
multiplyDragByParticleSize.html)| When using Drag, the drag strength will be
multiplied by the size of the particles if this toggle is enabled.  
[multiplyDragByParticleVelocity](ParticleSystemForceField-
multiplyDragByParticleVelocity.html)| When using Drag, the drag strength will
be multiplied by the speed of the particles if this toggle is enabled.  
[rotationAttraction](ParticleSystemForceField-rotationAttraction.html)|
Controls how strongly particles are dragged into the vortex motion.  
[rotationRandomness](ParticleSystemForceField-rotationRandomness.html)| Apply
randomness to the Force Field axis that particles will travel around.  
[rotationSpeed](ParticleSystemForceField-rotationSpeed.html)| The speed at
which particles are propelled around a vortex.  
[shape](ParticleSystemForceField-shape.html)| Selects the type of shape used
for influencing particles.  
[startRange](ParticleSystemForceField-startRange.html)| Setting a value
greater than 0 creates a hollow Force Field shape. This will cause particles
to not be affected by the Force Field when closer to the center of the volume
than the startRange property.  
[vectorField](ParticleSystemForceField-vectorField.html)| Apply forces to
particles within the volume of the Force Field, by using a 3D texture
containing vector field data.  
[vectorFieldAttraction](ParticleSystemForceField-vectorFieldAttraction.html)|
Controls how strongly particles are dragged into the vector field motion.  
[vectorFieldSpeed](ParticleSystemForceField-vectorFieldSpeed.html)| The speed
at which particles are propelled through the vector field.  
  
### Inherited Members

### Properties

[enabled](Behaviour-enabled.html)| Enabled Behaviours are Updated, disabled
Behaviours are not.  
---|---  
[isActiveAndEnabled](Behaviour-isActiveAndEnabled.html)| Reports whether a
GameObject and its associated Behaviour is active and enabled.  
[gameObject](Component-gameObject.html)| The game object this component is
attached to. A component is always attached to a game object.  
[tag](Component-tag.html)| The tag of this game object.  
[transform](Component-transform.html)| The Transform attached to this
GameObject.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[BroadcastMessage](Component.BroadcastMessage.html)| Calls the method named
methodName on every MonoBehaviour in this game object or any of its children.  
---|---  
[CompareTag](Component.CompareTag.html)| Checks the GameObject's tag against
the defined tag.  
[GetComponent](Component.GetComponent.html)| Gets a reference to a component
of type T on the same GameObject as the component specified.  
[GetComponentInChildren](Component.GetComponentInChildren.html)| Gets a
reference to a component of type T on the same GameObject as the component
specified, or any child of the GameObject.  
[GetComponentIndex](Component.GetComponentIndex.html)| Gets the index of the
component on its parent GameObject.  
[GetComponentInParent](Component.GetComponentInParent.html)| Gets a reference
to a component of type T on the same GameObject as the component specified, or
any parent of the GameObject.  
[GetComponents](Component.GetComponents.html)| Gets references to all
components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](Component.GetComponentsInChildren.html)| Gets
references to all components of type T on the same GameObject as the component
specified, and any child of the GameObject.  
[GetComponentsInParent](Component.GetComponentsInParent.html)| Gets references
to all components of type T on the same GameObject as the component specified,
and any parent of the GameObject.  
[SendMessage](Component.SendMessage.html)| Calls the method named methodName
on every MonoBehaviour in this game object.  
[SendMessageUpwards](Component.SendMessageUpwards.html)| Calls the method
named methodName on every MonoBehaviour in this game object and on every
ancestor of the behaviour.  
[TryGetComponent](Component.TryGetComponent.html)| Gets the component of the
specified type, if it exists.  
[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
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

