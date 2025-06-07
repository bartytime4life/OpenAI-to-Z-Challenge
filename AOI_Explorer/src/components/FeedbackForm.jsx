import { useState } from 'react';
import { Modal } from '@/components/ui/modal';
import { Textarea } from '@/components/ui/textarea';
import { Button } from '@/components/ui/button';

export default function FeedbackForm({ aoiId, onClose }) {
  const [notes, setNotes] = useState('');
  const [status, setStatus] = useState(null);

  const submitFeedback = async () => {
    try {
      const res = await fetch('/feedback', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ AOI_ID: aoiId, notes, timestamp: new Date().toISOString() })
      });
      if (res.ok) {
        setStatus('success');
        setTimeout(onClose, 1000);
      } else {
        setStatus('error');
      }
    } catch (e) {
      setStatus('error');
    }
  };

  return (
    <Modal isOpen={true} onClose={onClose}>
      <Modal.Title>Field Feedback for AOI {aoiId}</Modal.Title>
      <Modal.Content>
        <Textarea
          placeholder="Enter field notes here..."
          value={notes}
          onChange={(e) => setNotes(e.target.value)}
        />
        {status === 'success' && <p className="text-green-600 mt-2">Feedback submitted!</p>}
        {status === 'error' && <p className="text-red-600 mt-2">Submission failed.</p>}
      </Modal.Content>
      <Modal.Footer>
        <Button variant="secondary" onClick={onClose}>Cancel</Button>
        <Button onClick={submitFeedback} disabled={!notes}>Submit</Button>
      </Modal.Footer>
    </Modal>
  );
}